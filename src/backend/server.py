from flask import Flask  # módulo de servidor
from flask_cors import CORS  # módulo para evitar erros de CORS

app = Flask(__name__)
CORS(app)


@app.route('/magnet_state')
def get_magnet_state():
    return {
        "greeting": ["hello", "world"],
        "date": 1
    }

if __name__ == "__name__":
    app.run()