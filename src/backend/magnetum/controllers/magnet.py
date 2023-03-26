from magnetum.models.MagnetClass import Magnet

magnets = Magnet()

def get_current():
    try:
        state = magnets.get_state()
        intensity = magnets.get_intensity() # Pega valor booleano do JSON
        response = {'magnet_state': state, 'magnet_intensity': intensity}
        return response, 200
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def disable():  
    return magnets.disable()

def enable():  
    return magnets.enable()
    
def get_state(): 
    return magnets.get_state()

def get_intensity(): 
    return magnets.get_intensity()