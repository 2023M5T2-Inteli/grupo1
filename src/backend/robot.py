from serial.tools import list_ports
import time

import pydobot

home = (226, 0, 150, 0)

tray_coordinates = [
    (14, -225, 50, -86), # bandeja 1 - inicio_alto
    (14, -251, -44, -86), # bandeja 1 - inicio_baixo
    (182, -251, -44, -53), # bandeja 1 - final_baixo
    (182, -251, 50, -53), # bandeja 1 - final_alto

    (252, -100, 50, 22), # bandeja 2 - inicio_alto
    (252, -100, -44, 22), # bandeja 2 - inicio_baixo
    (248, 77, -44, 61),# bandeja 2 - final_baixo
    (248, 77, 50, 61),# bandeja 2 - final_alto

    (224, 226, 50, 88), # bandeja 3 - inicio_alto
    (224, 226, -44, 88), # bandeja 3 - inicio_baixo
    (34, 248, -44, 88), # bandeja 3 - final_baixo
    (34, 248, 50, 88), # bandeja 3 - final_alto

    (224, 226, 50, 88), # meio ponto de volta
    (182, -251, 50, -53), # meio ponto de volta
]

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[-1].device
device = pydobot.Dobot(port='COM7', verbose=False)

def execute_cycle():
    for coordinate in tray_coordinates:
        device.move_to(*coordinate, wait=True)

def rehome():
    device.move_to(*home, wait=True)

#(x, y, z, r, j1, j2, j3, j4) = device.pose()
#print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

#device.close()
