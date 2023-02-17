import machine
import time
import network
import urequests

ssid = 'ratos'
password = 'ratos!!!'

ima1 = machine.PWM(machine.Pin(16, machine.Pin.OUT))
ima2 = machine.PWM(machine.Pin(15, machine.Pin.OUT))

def ligar_ima(voltage):
    ima1.freq(1000)
    ima2.freq(1000)
    ima2.duty_u16(0)
    
    print(int(voltage / 12.0 * 65535))
    ima1.duty_u16(int(voltage / 12.0 * 65535))
    
def desligar_ima():
    ima1.freq(1000)
    ima2.freq(1000)
    ima1.duty_u16(0)
    ima2.duty_u16(0)
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    print(wlan.ifconfig())

#try:
ligar_ima(12)
time.sleep(100)
    #connect()
    
    #while True:
    #    ima_state = urequests.get('http://192.168.53.42:5000/ima')
    #    if(int(ima_state.text)):
     #       ligar_ima()
      #  else:
       #     desligar_ima()
        #time.sleep(0.1)

#except KeyboardInterrupt:
 #   machine.reset()
