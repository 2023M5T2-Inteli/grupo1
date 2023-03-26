from flask import request 

def init_app(app):

    @app.route('/change_tray', methods=['POST'])
    def tray():
        try:
            global current_tray
            json_input = int(request.json['current_tray']) # Pega valor booleano do JSON
            if json_input in [0, 1, 2, 3]:
                current_tray = json_input
                response = {'status': 'success', 'message': 'tray changed'}
            else:
                response = {'status': 'error', 'message': 'invalid value for tray parameter'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response
   