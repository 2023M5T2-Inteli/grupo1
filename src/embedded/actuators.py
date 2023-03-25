# Definição de classes de atuadores de ponte H. Como em nosso projeto o sentido da rotação não importa, 
# criamos classes em que um pino da ponte H fica sempre desligado (base) enquanto o outro varia
# conforme o estado desejado (enabler)

from machine import PWM, Pin

# Atuadores simples (sem PWM)
class Actuator:

    # Constantes de estado
    ON = 1
    OFF = 0

    def __init__(self, base, enabler):
        self.base = Pin(base, Pin.OUT)
        self.enabler = Pin(enabler, Pin.OUT)
        self.configureBase() 
        
    # Desliga a base
    def configureBase(self):
        self.base.value(Actuator.OFF)

    def enable(self):
        self.enabler.value(Actuator.ON)

    def disable(self):
        self.enabler.value(Actuator.OFF)
    
# Atuadores de PWM. A diferença é que se usa funções de PWM (.duty_u16()) em vez de digitais (.value())
# e se considera a intensidade máxima para o atual (12V, por exemplo) no cálculo do duty cycle 
class PWMActuator(Actuator):

    # Frequência de PWM a ser utilizada
    FREQUENCY = 1000

    def __init__(self, base, enabler, max_intensity):
        self.base = PWM(Pin(base, Pin.OUT))
        self.enabler = PWM(Pin(enabler, Pin.OUT))
        self.max_intensity = max_intensity # Intensidade máxima do PWM
        self.configureBase()
        self.setFrequency()
    
    def configureBase(self):
        self.base.duty_u16(Actuator.OFF)
    
    def setFrequency(self):
        self.base.freq(PWMActuator.FREQUENCY)
        self.enabler.freq(PWMActuator.FREQUENCY)

    def enable(self, intensity):
        MAX_DUTY_U16 = 65535 # Valor máximo de duty cycle 
        # Cálculo do duty cycle desejado através da proporção da
        # intensidade desejada em relação à intensidade máxima
        duty_cycle = int(intensity / float(self.max_intensity) * MAX_DUTY_U16)
        self.enabler.duty_u16(duty_cycle)

    def disable(self):
        self.enabler.duty_u16(Actuator.OFF)