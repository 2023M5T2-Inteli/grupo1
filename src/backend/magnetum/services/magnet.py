from magnetum.utils import State

magnet_state = State.OFF 

def disable_magnet():  
        global magnet_state
        magnet_state = State.OFF


def enable_magnet():  
    global magnet_state
    magnet_state = State.ON
    
def state_magnet(): 
    global magnet_state
    return magnet_state