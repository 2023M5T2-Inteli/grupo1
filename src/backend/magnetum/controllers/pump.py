from magnetum.models.Pump import Pump

pumps = Pump()
 

def get_current():
    try:
        state = pumps.get_state()
        response = {'pump_state': state}
        return response, 200
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
    
def set_current(request):
    try:
        state = request.json['pump_state']
        if state == True:
            pumps.enable()
        elif state == False:
            pumps.disable()
        response = {'pump_state': state}
        return response, 204
    
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
