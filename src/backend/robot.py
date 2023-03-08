# Código para controlar o robô. Utiliza a API 'pydobot' para se comunicar serialmente com o Magician Lite

# Importa bibliotecas necessárias
import pydobot  # Controla robô
import time
import requests

# Especificação da porta em que o robô está conectado.
# TO-DO: conexão sem especificar porta antes, já que ela muda de PC para PC (talvez um loop testando todas as possíveis, com try-catch?)
robot_port = 'COM7'
host = 'http://10.128.20.240:5000'


# Coordenadas do ponto neutro do robô segundo especificação técnica
home = (226, 0, 150, 0)

# Pontos reutilizáveis para a altura do robô e rotação da garra
high_height = 70
low_height = -32
rotation = -86

tray1 = [
    (35, -248, high_height, rotation),  # Ponto alto inicial
    (35, -248, low_height, rotation),  # Ponto baixo inicial
    (216, -248, low_height, rotation),  # Ponto baixo final
    (216, -248, high_height, rotation),  # Ponto alto final
]

tray2 = [
    (263, -112, high_height, rotation),  # Ponto alto inicial
    (263, -112, low_height, rotation),  # Ponto baixo inicial
    (263, 68, low_height, rotation),  # Ponto baixo final
    (263, 68, high_height, rotation),  # Ponto alto final
]

tray3 = [
    (222, 255, high_height, rotation),  # Ponto alto inicial
    (222, 255, low_height, rotation),  # Ponto baixo inicial
    (19, 255, low_height, rotation),  # Ponto baixo final
    (19, 255, high_height, rotation),  # Ponto alto final
]

intermediary_points = [
    (222, 255, high_height, rotation),  # Ponto alto inicial da bandeja 3
    (216, -248, high_height, rotation)  # Ponto alto inicial da bandeja 2
]
# Coordenadas para o movimento simples do robô
trays = [
    # BANDEJA 1
    tray1, tray2, tray3, intermediary_points
]

device = pydobot.Dobot(port=robot_port, verbose=False)

# Executa ciclo do ensaio conforme coordenadas do array


def execute_cycle():
    device.suck(True)  # Inicia sucção para segurar o ímã na demo atual
    time.sleep(1)
    requests.post(host + '/toggle_magnet', json = {"magnet_state": 1})
    for coordinate in tray1:
        device.move_to(*coordinate, wait=True)
    requests.post(host + '/toggle_pump', json = {"pump_state": 1})
    for coordinate in tray2:
        device.move_to(*coordinate, wait=True)
    requests.post(host + '/toggle_pump', json = {"pump_state": 0})
    for coordinate in tray3:
        device.move_to(*coordinate, wait=True)
        requests.post(host + '/toggle_magnet', json = {"magnet_state": 0})
# Move robô para ponto neutro utilizando variável de coordenadas do ponto home


def rehome():
    device.move_to(*home, wait=True)
