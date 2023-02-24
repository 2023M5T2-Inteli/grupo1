from flask import Flask
import robot
from flask_cors import CORS
import time

trialIsRunning = False
cycle_count = 0
ima_state = 0
pump_state = 0

app = Flask(__name__)
CORS(app)


@app.route('/start_trial')
def start_trial():
    print('Start trial')
    execute_trial()
    return 'Iniciou'


@app.route('/states')
def get_states():
    global ima_state 
    global pump_state   
    return str({"magnet": ima_state, "pump": pump_state})

@app.route('/magnet_state')
def get_magnet_state():
    global ima_state 
    return str(ima_state)

@app.route('/pump_state')
def get_pump_state():
    global pump_state 
    return str(pump_state)

@app.route('/desligar_ima')
def desligar_ima_rota():
    desligar_ima()
    print(ima_state)
    return 'desligado'

def desligar_ima():
    global ima_state
    ima_state = 0

def ligar_ima():
    global ima_state
    ima_state = 1

def ligar_bomba():
    global pump_state
    pump_state = 1

def desligar_bomba():
    global pump_state
    pump_state = 0

@app.route('/ligar_ima')
def ligar_ima_rota():
    ligar_ima()
    return 'ligado'

@app.route('/ligar_bomba')
def ligar_bomba_rota():
    ligar_bomba()
    return 'ligado'

@app.route('/desligar_bomba')
def desligar_bomba_rota():
    desligar_bomba()
    return 'desligado'

def execute_trial():
    robot.rehome()
    for i in range(5):
        robot.execute_cycle()
        incrementCycle()


def incrementCycle():
    global cycle_count
    cycle_count = cycle_count + 1


@app.route('/cycleCount')
def getCycleCount():
    global cycle_count
    return str(cycle_count)



