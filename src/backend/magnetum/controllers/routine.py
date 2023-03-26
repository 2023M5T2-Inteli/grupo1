from magnetum.blueprints import robot

cycles_per_trial = 5

cycle_count = 0 # Contagem de ciclo atual do robô (quantas passadas ele já fez no ensaio atual)

current_tray = 0

def execute_trial():
        restartCycleCount()  
        robot.rehome()  # Função do módulo do robô para levá-lo ao ponto neutro
        # Loop para realizar um número arbitrário de passadas.
        for i in range(cycles_per_trial):
            robot.execute_cycle()  
            incrementCycle()  
        global current_tray
        current_tray = 0

def restartCycleCount():
        global cycle_count
        cycle_count = 0

def incrementCycle():
        global cycle_count  
        cycle_count = cycle_count + 1  

def getCurrentCycle():
        global cycle_count
        return cycle_count