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
    
def set_current(request):
    try:
        state = request.json['magnet_state']
        intensity = request.json['magnet_intensity']
        magnets.set_intensity(intensity)
        if state == True:
            magnets.enable()
        elif state == False:
            magnets.disable()
        response = {'magnet_state': state, 'magnet_intensity': intensity}
        return response, 204
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
