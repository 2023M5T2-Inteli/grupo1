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
host = 'http://10.128.65.51:5000'

magnet_max_voltage = 12

# Definição dos ímãs.
# Cada objeto corresponde a dois ímãs ligados em paralelo a um lado da ponte H. Utilizamos PWM para variar a intesidade.
magnets = [PWMActuator(2, magnet_max_voltage), PWMActuator(3, magnet_max_voltage)]
pumps = [Actuator(27), Actuator(26)]

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
        magnet = json.loads(urequests.get(host + '/current/magnet').text)
        pump = json.loads(urequests.get(host + '/current/pump').text)
        
        print(magnet)
        print(pump)

        # Liga ímãs se o valor lido no servidor for maior que 0
        if (int(magnet['magnet_state'])):
            magnets[0].enable(intensity=magnet['magnet_intensity'])
            magnets[1].enable(intensity=magnet['magnet_intensity'])
            
        else: # Desliga se for 0
            magnets[0].disable()
            magnets[1].disable()

        # Liga bombas se o valor lido no servidor for maior que 0
        if (int(pump['pump_state'])):
            print('ligar')
            # Acessa cada elemento do array de bombas e executa a função de ligar
            pumps[0].enable()
            pumps[1].enable()
        else: # Desliga se for 0
            pumps[0].disable()
            pumps[1].disable()
        time.sleep(0.1)
        
except KeyboardInterrupt:
    reset()