# Código para controlar o Raspberry Pi Pico W. Em suma, o microcontrolador se conecta à rede local
# e então envia requisições continuamente ao servidor para descobrir o estado desejado para os atuadores. Segundo as informações recebidas, ele liga ou desliga os componentes externos (ímã e bomba)

# Importa bibliotecas necessárias
import machine  # Controla o Raspberry
import time  # Permite adicionar delays ao programa
import network  # Permite conexão
import urequests  # Permite envio de requisições

# Definição da rede local a ser utilizada
ssid = 'Inteli-COLLEGE'
password = 'QazWsx@123' 
# Definição do endereço do servidor na rede atual
host = 'http://10.128.20.240:5000'

# Definição dos pinos do ímã como PWM e output
magnet_pin_1 = machine.PWM(machine.Pin(16, machine.Pin.OUT))
magnet_pin_2 = machine.PWM(machine.Pin(15, machine.Pin.OUT))
# Define frequências dos pinos dos ímãs
magnet_pin_1.freq(1000)
magnet_pin_2.freq(1000)

# Definição dos pinos da bomba como pinos digitais de output. Como a intensidade da bomba não precisa ser dinâmica, não precisamos utilizar PWM
pump_pin_1 = machine.Pin(12, machine.Pin.OUT)
pump_pin_2 = machine.Pin(13, machine.Pin.OUT)

# Definição do pino do LED e do sensor de fluxo eletromagnético para testes
led = machine.Pin(18, machine.Pin.OUT)
sensor = machine.ADC(28)

# Esta função liga o ímã na voltagem desejada. A integração com o front passando essa voltagem
# ainda não foi implementada, então, por enquanto, essa função é sempre executada com argumento
# 'hardcoded' 12.
def enable_magnet(voltage):
    # Seguindo a lógica do ponte H, desligamos um dos pinos e ligamos a proporção desejada no outro
    magnet_pin_2.duty_u16(0)
    # O argumento dessa função encontra o valor proporcional de duty cycle a ser enviado para
    # o ímã, transformando um valor na escala 0-12 para um valor na escala 0-65535
    magnet_pin_1.duty_u16(int(voltage / 12.0 * 65535))

# Desliga o ímã, enviando a ambos os pinos 0
def disable_magnet():
    magnet_pin_1.duty_u16(0)
    magnet_pin_2.duty_u16(0)

# Liga a bomba, enviando a apenas um pino 1, seguindo a lógica da ponte H
def enable_pump():
    pump_pin_1.value(1)
    pump_pin_2.value(0)

# Desliga a bomba, enviando a ambos os pinos 0
def disable_pump():
    pump_pin_1.value(0)
    pump_pin_2.value(0)

# Liga a sensor
def enable_sensor():
    sensor_pin.value(1)

# Desliga a sensor
def disable_sensor():
    sensor_pin.value(0)

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
        #sensor_state = urequests.get(host + '/pump_state')
        
        # Liga ímã com voltagem 12 se o valor lido no servidor for maior que zero
        if (int(magnet_state.text)):
            enable_magnet(12)
        else: # Desliga se for 0
            disable_magnet()

        # Liga bomba se o valor lido no servidor for maior que zero
        if (int(pump_state.text)):
            enable_pump()
        else: # Desliga se for 0
            disable_pump()

        # Liga sensor se o valor lido no servidor for maior que zero
        if (int(sensor_state.text)):
            enable_sensor()
        else: # Desliga se for 0
            disable_sensor()    

        # Liga o LED se o sensor captar fluxo eletromagnético. TO-DO: transformar leitura em analógica e printar valores a cada segundo.
        print(sensor.read_u16())
        #if (int(sensor_state.text) == 1 and sensor.value() == 1):
            #led.value(1)
        #else:
            #led.value(0)

        # Espera 0.1s antes de reiniciar o loop
        time.sleep(0.1)
        
except KeyboardInterrupt:
    machine.reset()
