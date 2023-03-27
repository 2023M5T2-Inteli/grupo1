# Especialização da classe de atuadores para bombas

from magnetum.models.Actuator import Actuator
    
class Pump(Actuator):
    def __init__(self):
        Actuator.__init__(self)
