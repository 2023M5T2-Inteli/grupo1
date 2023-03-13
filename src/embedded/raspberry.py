# Código para controlar o Raspberry Pi Pico W. Em suma, o microcontrolador se conecta à rede local
# e então envia requisições continuamente ao servidor para descobrir o estado desejado para os 
# atuadores. Segundo as informações recebidas, ele liga ou desliga os componentes externos (ímã e bomba).

from machine import reset # Controla o Raspberry
import time 
import network  # Permite conexão
import urequests  # Permite envio de requisições
from actuators import * # Classes para atuadores

# Definição da rede local a ser utilizada
ssid = 'Inteli-COLLEGE'
password = 'QazWsx@123' 
host = 'http://10.128.64.149:5000/'

magnet_max_voltage = 12

# Definição dos ímãs.
# Cada objeto corresponde a dois ímãs ligados em paralelo a um lado da ponte H. Utilizamos PWM para variar a intesidade.
magnets = [PWMActuator(10, 11, magnet_max_voltage), PWMActuator(9, 8, magnet_max_voltage)]

# Definição das bombas d'água. Não precisamos utilizar PWM, pois não variaremos a intensidade.
pumps = [Actuator(0, 1), Actuator(2, 3)]

def connectToWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)

    # Printa informações de conexão
    print(wlan.ifconfig())


# Código a ser executado quando o Raspberry é ligado
try:
    connectToWiFi() 
    while True:  # Loop principal do programa
        # Ainda não descobrimos como processar um objeto json em micropython. Por isso,
        # por ora estamos utilizando rotas separadas para cada estado.
        magnet_state = urequests.get(host + '/magnet_state')
        pump_state = urequests.get(host + '/pump_state')
        
        print('Magnet: ' + magnet_state.text)
        print('Pump: ' + pump_state.text)

        # Liga ímãs se o valor lido no servidor for maior que 0
        if (int(magnet_state.text)):
            map(lambda magnet: magnet.enable(), magnets)
        else: # Desliga se for 0
            map(lambda magnet: magnet.disable(), magnets)

        # Liga bombas se o valor lido no servidor for maior que 0
        if (int(pump_state.text)):
            # Acessa cada elemento do array de bombas e executa a função de ligar
            map(lambda pump: pump.enable(), pumps)
        else: # Desliga se for 0
            map(lambda pump: pump.disable(), pumps)

        time.sleep(0.1)
        
except KeyboardInterrupt:
    reset()
