# Código para controlar o Raspberry Pi Pico W. Em suma, o microcontrolador se conecta à rede local
# e então envia requisições continuamente ao servidor para descobrir o estado desejado para os 
# atuadores. Segundo as informações recebidas, ele liga ou desliga os componentes externos (ímã e bomba).

from machine import reset # Controla o Raspberry
import time 
import network  # Permite conexão
import urequests  # Permite envio de requisições
from actuators import * # Classes para atuadores
import json

# Definição da rede local a ser utilizada
ssid = 'Inteli-COLLEGE'
password = 'QazWsx@123' 
host = 'http://10.128.0.159:5000'

magnet_max_voltage = 12

# Definição dos ímãs.
# Cada objeto corresponde a dois ímãs ligados em paralelo a um lado da ponte H. Utilizamos PWM para variar a intesidade.
magnets = [PWMActuator(12, magnet_max_voltage), PWMActuator(10, magnet_max_voltage)]
pumps = [Actuator(18, magnet_max_voltage), Actuator(20, magnet_max_voltage)]

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
        magnet_state = urequests.get(host + '/current/magnet')
        pump_state = urequests.get(host + '/current/pump')
        magnet_intensity = urequests.get(host + '/magnet_intensity')
        
        print('Magnet: ' + magnet_state.text)
        print('Pump: ' + pump_state.text)
        print('Magnet Intensity: ' + magnet_intensity.text)

        # Liga ímãs se o valor lido no servidor for maior que 0
        if (int(magnet_state.text)):
            map(lambda magnet: magnet.enable(intensity=magnet_intensity), magnets)
            
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