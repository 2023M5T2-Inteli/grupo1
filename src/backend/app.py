from flask import Flask
import robot
from flask_cors import CORS
import time

trialIsRunning = False
cycle_count = 0

app = Flask(__name__)
CORS(app)


@app.route('/start_trial')
def start_trial():
    print('Start trial')
    execute_trial()
    return 'Iniciou'


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
