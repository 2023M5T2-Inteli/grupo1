# Código para controlar o Raspberry Pi Pico W. Em suma, o microcontrolador se conecta à rede local
# e então envia requisições continuamente ao servidor para descobrir o estado desejado para os atuadores. Segundo as informações recebidas, ele liga ou desliga os componentes externos (ímã e bomba)

# Importa bibliotecas necessárias
from machine import PWM, Pin # Controla o Raspberry
import time  # Permite adicionar delays ao programa
import network  # Permite conexão
import urequests  # Permite envio de requisições

# Definição da rede local a ser utilizada
ssid = 'Inteli-COLLEGE'
password = 'QazWsx@123' 
# Definição do endereço do servidor na rede atual
host = 'http://10.128.20.240:5000'

# Definição dos pinos do ímã como PWM e output
magnets_a = [PWM(machine.Pin(16, machine.Pin.OUT)),
           PWM(machine.Pin(16, machine.Pin.OUT))]

magnets_b = [PWM(machine.Pin(16, machine.Pin.OUT)),
           PWM(machine.Pin(16, machine.Pin.OUT))]

for magnet in magnets_a:
    magnet.freq(1000)
    
for magnet in magnets_b:
    magnet.freq(1000)

# Definição dos pinos da bomba como pinos digitais de output. Como a intensidade da bomba não precisa ser dinâmica, não precisamos utilizar PWM
shaker_pump_pin_1 = Pin(12, Pin.OUT)
shaker_pump_pin_2 = Pin(13, Pin.OUT)

cleaner_pump_pin_1 = machine.Pin(14, machine.Pin.OUT)
cleaner_pump_pin_2 = machine.Pin(15, machine.Pin.OUT)

# Esta função liga o ímã na voltagem desejada. A integração com o front passando essa voltagem
# ainda não foi implementada, então, por enquanto, essa função é sempre executada com argumento
# 'hardcoded' 12.
def enable_magnets(voltage):
    max_voltage = 12.0
    max_duty_u16 = 65535
    magnets_a[0].duty_u16(0)
    magnets_b[0].duty_u16(0)

    magnets_a[1].duty_u16(int(voltage / max_voltage * max_duty_u16))
    magnets_b[1].duty_u16(int(voltage / max_voltage * max_duty_u16))

# Desliga o ímã, enviando a ambos os pinos 0
def disable_magnet():
    magnets_a[1].duty_u16(0)
    magnets_b[1].duty_u16(0)

# Liga a bomba, enviando a apenas um pino 1, seguindo a lógica da ponte H
def enable_pump():
    shaker_pump_pin_1.value(1)
    shaker_pump_pin_2.value(0)

# Desliga a bomba, enviando a ambos os pinos 0
def disable_pump():
    shaker_pump_pin_1.value(0)
    shaker_pump_pin_2.value(0)

# Conecta à rede local
def connect():
    # Cria e inicializa objeto de conexão WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Conecta à rede especificada com a respectiva senha
    wlan.connect(ssid, password)

    # Tenta conectar a cada 1 segundo
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)

    # Printa informações da conexão quando é bem-sucedida
    print(wlan.ifconfig())


# Código a ser executado quando o Raspberry é ligado
try:
    connect()  # Conecta à rede local
    while True:  # Loop para ler estado desejado dos atuadores
        # Ainda não descobrimos como processar um objeto json em micropython. Por isso,
        # por ora estamos utilizando rotas separadas para cada estado.
        magnet_state = urequests.get(host + '/magnet_state')
        pump_state = urequests.get(host + '/pump_state')
        
        print('Magnet: ' + magnet_state.text)
        print('Pump: ' + pump_state.text)

        
        # Liga ímã com voltagem 12 se o valor lido no servidor for maior que zero
        if (int(magnet_state.text)):
            enable_magnets(12)
        else: # Desliga se for 0
            disable_magnet()

        # Liga bomba se o valor lido no servidor for maior que zero
        if (int(pump_state.text)):
            enable_pump()
        else: # Desliga se for 0
            print('disable pump')
            disable_pump() 

        # Espera 0.1s antes de reiniciar o loop
        time.sleep(0.1)
        
except KeyboardInterrupt:
    machine.reset()
