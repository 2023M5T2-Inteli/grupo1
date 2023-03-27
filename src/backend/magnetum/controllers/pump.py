# Funções para manipulação dos estados das bombas d'água

from magnetum.models.Pump import Pump

pumps = Pump()
 
# Devolve estado atual das bombas
def get_current():
    try:
        state = pumps.get_state()
        response = {'pump_state': state}
        return response, 200
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
    
# Define estado atual das bombas
def set_current(request):
    try:
        state = request.json['pump_state']
        if state == True:
            pumps.enable()
        elif state == False:
            pumps.disable()
        response = {'pump_state': state}
        return response, 200
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
