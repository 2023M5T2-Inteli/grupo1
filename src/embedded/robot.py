from serial.tools import list_ports
import time

import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[-1].device

device = pydobot.Dobot(port=port, verbose=False)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.move_to(10, -227, -23, -57, wait=True)
device.move_to(145, -231, -41, -57, wait=True)
device.move_to(156, -229, 110, -55, wait=True)
device.move_to(251, -79, 114, -17, wait=True)
device.move_to(281, -85, -32, -16, wait=True)
device.move_to(285, 64, -29, 12, wait=True)


device.close()