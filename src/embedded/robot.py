from serial.tools import list_ports
import time

import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[-1].device

device = pydobot.Dobot(port=port, verbose=False)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.move_to(x + 50, y + 50, z - 10, r+ 200, wait=True)

device.close()