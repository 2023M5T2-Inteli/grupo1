# Especificação da classe de ímãs com intensidade

from magnetum.models.Actuator import Actuator

class Magnet(Actuator):
    def __init__(self):
        Actuator.__init__(self)
        self.intensity = 12
    
    def set_intensity(self, intensity):
        self.intensity = intensity

    def get_intensity(self):
        return self.intensity
    