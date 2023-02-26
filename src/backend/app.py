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
# 5. Definir se rotas serão em inglês ou português

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
    restartCycleCount() # Reinicia contagem de ciclos
    robot.rehome() # Função do módulo do robô para levá-lo ao ponto neutro
    for i in range(5): # Loop para realizar 5 passadas. Esse argumento se tornará dinâmico nas próximas
                        # sprints. Está assim agora apenas para testes.
        robot.execute_cycle() # Executa o ciclo segundo função do módulo do robô
        incrementCycle() # Incrementa variável de contagem dos ciclos atuais

@app.route('/cycleCount') # Rota para ler número de ciclos (passadas) atual
def getCycleCount():
    global cycle_count
    return str(cycle_count)

def restartCycleCount():
    global cycle_count
    cycle_count = 0

def incrementCycle():
    global cycle_count # Chama variável global de contagem
    cycle_count = cycle_count + 1 # Incrementa variável

# CÓDIGO PARA LER ESTADOS DO ÍMÃ E DA BOMBA

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

# CÓDIGO PARA MODIFICAR ESTADO DO ÍMÃ 
# Nesse caso, foi preciso separar as rotas das funções que modificam os valores, por serem variáveis
# globais. Quando tentamos deixar tudo na mesma função da rota, o programa apresentava erros.

@app.route('/enable_magnet') # Rota para ligar ímã
def enable_magnet_route():
    enable_magnet()
    return 'magnet on'

@app.route('/disable_magnet') # Rota para desligar o ímã
def disable_magnet_route():
    disable_magnet()
    return 'magnet off'

def disable_magnet(): # Modifica estado do ímã para 0
    global magnet_state
    magnet_state = 0

def enable_magnet(): # Modifica estado do ímã para 1
    global magnet_state
    magnet_state = 1

# CÓDIGO PARA MODIFICAR ESTADO DA BOMBA
# Nesse caso, foi preciso separar as rotas das funções que modificam os valores, por serem variáveis
# globais. Quando tentamos deixar tudo na mesma função da rota, o programa apresentava erros.

@app.route('/enable_pump') # Rota para ligar bomba
def enable_pump_route():
    enable_pump()
    return 'pump on'

@app.route('/disable_pump') # Rota para desligar bomba
def disable_pump_route():
    disable_pump()
    return 'pump off'

def disable_pump(): # Modifica estado da bomba para 0
    global pump_state
    pump_state = 0

def enable_pump(): # Modifica estado da bomba para 1
    global pump_state
    pump_state = 1
