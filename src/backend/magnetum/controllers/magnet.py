from magnetum.models.Magnet import Magnet

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
        intensity = request.json['magnet_intensity'] or magnets.get_intensity()
        if intensity in range(0, 13):
            magnets.set_intensity(intensity)
        else:
            response = {'status': 'error', 'message': 'intensity must be between 0 and 12'}
            return response, 500
        if state == True:
            magnets.enable()
        elif state == False:
            magnets.disable()
        else:
            response = {'status': 'error', 'message': 'state must be True or False'}
            return response, 500
        response = {'magnet_state': state, 'magnet_intensity': intensity}
        return response, 200
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
