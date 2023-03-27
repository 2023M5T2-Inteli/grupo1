# Funções para interagir com estados dos ímãs

from magnetum.models.Magnet import Magnet

magnets = Magnet()

# Devolve estado atual dos ímãs
def get_current():
    try:
        state = magnets.get_state()
        intensity = magnets.get_intensity() # Pega valor booleano do JSON
        response = {'magnet_state': state, 'magnet_intensity': intensity}
        return response, 200
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
    
# Define estado atual dos ímãs
def set_current(request):
    try:
        state = request.json['magnet_state']

        # Mantém estado atual se um novo não for especificado
        intensity = request.json['magnet_intensity'] or magnets.get_intensity()

        # Verifica se intensidade está entre 0 e 12
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
