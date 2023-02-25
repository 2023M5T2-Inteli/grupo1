# Este é o código do servidor/backend do sistema, que intermedia as comunicações entre o usuário
# final na interface gráfica e o robô/microcontrolador. Essas comunicações se dão através de diferentes
# rotas de leitura e mudança de estados, que alteram variáveis globais e executam funções específicas
# em cada subsistema.

# PRÓXIMAS PASSOS PARA ESTE CÓDIGO:
# 1. Modularizar em pasta de rotas, controladores e serviços
# 2. Transformar rotas de mudança de estados em POST em vez de GET
# 3. Aumentar dinamicidade dos serviços, com passagem de argumentos em POST
# 4. Resolver integração das rotas de estados com o front e raspberry (atualmente, temos rotas
# que retornam a mesma coisa de maneiras diferentes para cada subsistema)

# Importação dos módulos necessários
from flask import Flask # módulo de servidor
import robot # módulo personalizado para controlar o robô
from flask_cors import CORS # módulo para evitar erros de CORS

# Declaração de variáveis globais
cycle_count = 0 # Contagem de ciclo atual do robô (quantas passadas ele já fez no ensaio atual)
magnet_state = 0 # Estado do ímã (ligado/desligado)
pump_state = 0 # Estado da bomba d'água (ligada/desligada)

app = Flask(__name__) # Cria servidor
CORS(app) # Adiciona proteção contra erros CORS

# CÓDIGO REFERENTE AO ROBÔ
@app.route('/start_trial') # Rota para iniciar ensaio com o robô
def start_trial():
    execute_trial() # Chama função do servidor que organiza o ensaio
    return 'Trial started'

def execute_trial():
    robot.rehome() # Função do módulo do robô para levá-lo ao ponto neutro
    for i in range(5): # Loop para realizar 5 passadas. Esse argumento se tornará dinâmico nas próximas
                        # sprints. Está assim agora apenas para testes.
        robot.execute_cycle() # Executa o ciclo segundo função do módulo do robô
        incrementCycle() # Incrementa variável de contagem dos ciclos atuais

def incrementCycle():
    global cycle_count # Chama variável global de contagem
    cycle_count = cycle_count + 1 # Incrementa variável


# ROTAS PARA LER ESTADOS DO ÍMÃ E DA BOMBA

@app.route('/states') # Rota para devolver estado do ímã e da bomba em JSON. Atualmente integrado
# apenas com o front, porque não descobrimos como processar JSON no Raspberry ainda
def get_states():
    global magnet_state 
    global pump_state   
    return str({"magnet": magnet_state, "pump": pump_state})

@app.route('/magnet_state') # Rota que devolve apenas valor do estado do ímã para o Raspberry
def get_magnet_state():
    global magnet_state 
    return str(magnet_state)

@app.route('/pump_state') # Rota que devolve apenas valor do estado da bomba para o Raspberry
def get_pump_state():
    global pump_state 
    return str(pump_state)

#    

@app.route('/enable_magnet')
def enable_magnet_route():
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

@app.route('/desligar_ima')
def desligar_ima_rota():
    desligar_ima()
    print(magnet_state)
    return 'desligado'

def desligar_ima():
    global magnet_state
    magnet_state = 0

def ligar_ima():
    global magnet_state
    magnet_state = 1

def ligar_bomba():
    global pump_state
    pump_state = 1

def desligar_bomba():
    global pump_state
    pump_state = 0

@app.route('/cycleCount')
def getCycleCount():
    global cycle_count
    return str(cycle_count)



