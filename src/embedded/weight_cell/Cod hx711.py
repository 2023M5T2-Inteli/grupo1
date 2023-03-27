import machine
from hx711 import HX711
from time import sleep

# inicializando o modulo HX711 (DT, SCK)
hx = HX711(2, 3)
# valor base de medida
base = 128750

#Função para ler e retornar os valores da célula de carga
def readCell(load_cell):
    val = load_cell.read()
    print("Load cell value: ", val)
    return val

def convert(vl):
    wt = (vl - base)/1070
    print("Weight: ", wt)
    return wt
    
# Lendo o valor da célula de carga e printando
while True:
    value = readCell(hx)
    weight = convert(value)
    sleep(2)
    
    