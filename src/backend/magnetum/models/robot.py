# Código para controlar o robô. Utiliza a API 'pydobot' para se comunicar serialmente com o Magician Lite

import pydobot  # Controla robô
import requests
from magnetum.utils.State import State

# Especificação da porta em que o robô está conectado.
# TO-DO: conexão sem especificar porta antes, já que ela muda de PC para PC (talvez um loop testando todas as possíveis, com try-catch?)
robot_port = 'COM7'
host = 'http://10.128.0.159:5000'

# Coordenadas do ponto neutro do robô segundo especificação técnica
home = (226, 0, 150, 0)

# Pontos reutilizáveis para a altura do robô e rotação da garra
high_height = 77
low_height = -40
rotation = -86

tray1 = [
    (215, -155, high_height, rotation),  # Ponto alto inicial
    (215, -155, low_height, rotation),  # Ponto baixo inicial
    (315, -141, low_height, rotation),  # Ponto baixo final
    (315, -141, high_height, rotation),  # Ponto alto final
]

tray2 = [
    (326, 1, high_height, rotation),  # Ponto alto inicial
    #(263, -112, low_height, rotation),  # Ponto baixo inicial
    #(263, 68, low_height, rotation),  # Ponto baixo final
    (184, 1, high_height, rotation),  # Ponto alto final
]

tray3 = [
    (200, 157, high_height, rotation),  # Ponto alto inicial
    (200, 157, low_height, rotation),  # Ponto baixo inicial
    (311, 157, low_height, rotation),  # Ponto baixo final
    (311, 157, high_height, rotation),  # Ponto alto final
]

intermediary_points = [
    (222, 255, high_height, rotation),  # Ponto alto inicial da bandeja 3
    (216, -248, high_height, rotation)  # Ponto alto inicial da bandeja 2
]

#device = pydobot.Dobot(port=robot_port, verbose=False)

# Função para executar um ciclo completo do robô
def execute_cycle():
    device.speed(velocity=85, acceleration=50)
    rehome()

    requests.post(host + '/current/magnet', json = {"magnet_state": State.ON.value}) # Liga ímã
    requests.post(host + '/current/tray', json = {"current_tray": 1}) # Troca estado da bandeja


    for coordinate in tray1:
        device.move_to(*coordinate, wait=True)

    requests.post(host + '/current/pump', json = {"pump_state": State.ON.value}) # Liga bomba

    requests.post(host + '/current/tray', json = {"current_tray": 2}) # Troca estado da bandeja


    for coordinate in tray2:
        device.move_to(*coordinate, wait=True)
    requests.post(host + '/current/pump', json = {"pump_state": State.OFF.value}) # Desliga bomba

    requests.post(host + '/current/tray', json = {"current_tray": 3}) # Troca estado da bandeja

    for coordinate in tray3:
        device.move_to(*coordinate, wait=True)
        requests.post(host + '/current/magnet', json = {"magnet_state": State.OFF.value}) # Desliga ímã

def rehome():
    device.move_to(*home, wait=True)