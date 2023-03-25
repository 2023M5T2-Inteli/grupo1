from magnetum.utils import State

pump_state = State.OFF 
 
def disable_pump():  
    global pump_state
    pump_state = State.OFF

def enable_pump():  
    global pump_state
    pump_state = State.ON