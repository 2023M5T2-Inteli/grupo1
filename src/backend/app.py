from flask import Flask
import robot
from flask_cors import CORS
import time

trialIsRunning = False
cycle_count = 0
ima_state = 1

app = Flask(__name__)
CORS(app)


@app.route('/start_trial')
def start_trial():
    print('Start trial')
    execute_trial()
    return 'Iniciou'


@app.route('/ima')
def get_ima():
    global ima_state
    print('IMA STATE: ' + str(ima_state))  
    
    return str(ima_state)

@app.route('/desligar_ima')
def desligar_ima():
    desligar()
    print(ima_state)
    return 'desligado'

def desligar():
    global ima_state
    ima_state = 0

def ligar():
    global ima_state
    ima_state = 1

@app.route('/ligar_ima')
def ligar_ima():
    ligar()
    return 'ligado'

def execute_trial():
    robot.rehome()
    robot.device.move_to(182, -251, 50, -53)
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



