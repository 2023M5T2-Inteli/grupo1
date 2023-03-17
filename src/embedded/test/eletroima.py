import machine
import time

motor1 = machine.Pin(19, machine.Pin.OUT)
motor2 = machine.Pin(18, machine.Pin.OUT)
ima1 = machine.Pin(17, machine.Pin.OUT)
ima2 = machine.Pin(16, machine.Pin.OUT)

motor1.value(0)
motor2.value(1)
ima1.value(0)
ima2.value(1)

print('rodando')
time.sleep(10)
print('rodei')