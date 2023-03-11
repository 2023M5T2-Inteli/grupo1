# Código para controlar o robô. Utiliza a API 'pydobot' para se comunicar serialmente com o Magician Lite

# Importa bibliotecas necessárias
import pydobot # Controla robô
import time

# Especificação da porta em que o robô está conectado.
# TO-DO: conexão sem especificar porta antes, já que ela muda de PC para PC (talvez um loop testando todas as possíveis, com try-catch?)
<<<<<<< Updated upstream
robot_port = 'COM7' 
=======
robot_port = 'COM5'
host = 'http://10.128.64.149:5000'
>>>>>>> Stashed changes

home = (226, 0, 150, 0) # Coordenadas do ponto neutro do robô segundo especificação técnica

# Pontos reutilizáveis para a altura do robô e rotação da garra
high_height = 77
low_height = -40
rotation = -86

<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes
# Coordenadas para o movimento simples do robô
tray_coordinates = [
    # BANDEJA 1
    (35, -248, high_height, rotation), # Ponto alto inicial
    (35, -248, low_height, rotation), # Ponto baixo inicial
    (216, -248, low_height, rotation), # Ponto baixo final
    (216, -248, high_height, rotation), # Ponto alto final

    # BANDEJA 2
    (263, -112, high_height, rotation), # Ponto alto inicial
    (263, -112, low_height, rotation), # Ponto baixo inicial
    (263, 68, low_height, rotation), # Ponto baixo final
    (263, 68, high_height, rotation), # Ponto alto final

    # BANDEJA 3
    (222, 255, high_height, rotation), # Ponto alto inicial
    (222, 255, low_height, rotation), # Ponto baixo inicial
    (19, 255, low_height, rotation), # Ponto baixo final
    (19, 255, high_height, rotation), # Ponto alto final

    # PONTOS INTERMEDIÁRIOS PARA REINICIAR
    (222, 255, high_height, rotation), # Ponto alto inicial da bandeja 3
    (216, -248, high_height, rotation) # Ponto alto inicial da bandeja 2
]

device = pydobot.Dobot(port=robot_port, verbose=False)

# Executa ciclo do ensaio conforme coordenadas do array
def execute_cycle():
<<<<<<< Updated upstream
    device.suck(True) # Inicia sucção para segurar o ímã na demo atual
=======
    device.speed(velocity=75, acceleration=50)
    rehome()
    device.suck(True)  # Inicia sucção para segurar o ímã na demo atual
>>>>>>> Stashed changes
    time.sleep(1)
    for coordinate in tray_coordinates: # Move o robô para cada coordenada
            device.move_to(*coordinate, wait=True)
        
# Move robô para ponto neutro utilizando variável de coordenadas do ponto home
def rehome():
    device.move_to(*home, wait=True) 