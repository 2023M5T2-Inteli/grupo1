# Definição da dlasse geral para atuadores com manipulação de estado

from magnetum.utils.State import State

class Actuator():
    def __init__(self):
        self.state = State.OFF
    
    def disable(self):
        self.state = State.OFF
    
    def enable(self):
        self.state = State.ON
    
    def get_state(self):
        return self.state.value