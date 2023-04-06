# Enum para as bandejas do equipamento

from enum import Enum

class Tray(Enum):
    DESATIVADO = 0
    CAPTURA = 1
    LIMPEZA = 2
    DESPEJO = 3
