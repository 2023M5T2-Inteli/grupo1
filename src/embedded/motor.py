# Código para controlar o Raspberry Pi Pico W. Em suma, o microcontrolador se conecta à rede local
# e então envia requisições continuamente ao servidor para descobrir o estado desejado para os atuadores. Segundo as informações recebidas, ele liga ou desliga os componentes externos (ímã e bomba)

# Importa bibliotecas necessárias
from machine import PWM, Pin, reset # Controla o Raspberry
import time  # Permite adicionar delays ao programa
import network  # Permite conexão
import urequests  # Permite envio de requisições

# Definição da rede local a ser utilizada
ssid = 'Inteli-COLLEGE'
password = 'QazWsx@123' 
# Definição do endereço do servidor na rede atual
host = 'http://10.128.64.149:5000/'

# Definição dos pinos do ímã como PWM e output
magnets_a = [PWM(Pin(10, Pin.OUT)),
           PWM(Pin(11, Pin.OUT))]

magnets_b = [PWM(Pin(9, Pin.OUT)),
           PWM(Pin(8, Pin.OUT))]

for magnet in magnets_a:
    magnet.freq(1000)
    
for magnet in magnets_b:
    magnet.freq(1000)

# Definição dos pinos da bomba como pinos digitais de output. Como a intensidade da bomba não precisa ser dinâmica, não precisamos utilizar PWM
shaker_pump = [Pin(0, Pin.OUT), Pin(1, Pin.OUT)]

cleaner_pump = [Pin(2, Pin.OUT), Pin(3, Pin.OUT)]

def init():
    disable_magnets()
    disable_pumps()

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
def disable_magnets():
    magnets_a[1].duty_u16(0)
    magnets_b[1].duty_u16(0)

# Liga a bomba, enviando a apenas um pino 1, seguindo a lógica da ponte H
def enable_pumps():
    shaker_pump[0].value(0)
    cleaner_pump[0].value(0)
    shaker_pump[1].value(1)
    cleaner_pump[1].value(1)

# Desliga a bomba, enviando a ambos os pinos 0
def disable_pumps():
    shaker_pump[1].value(0)
    cleaner_pump[1].value(0)

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
    init()
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
            disable_magnets()

        # Liga bomba se o valor lido no servidor for maior que zero
        if (int(pump_state.text)):
            enable_pumps()
        else: # Desliga se for 0
            print('disable pump')
            disable_pumps() 

        # Espera 0.1s antes de reiniciar o loop
        time.sleep(0.1)
        
except KeyboardInterrupt:
    reset()
