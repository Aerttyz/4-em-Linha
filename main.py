# Módulos nativos
from pathlib import Path
import sys

# Paths (insira o seu logo abaixo)
path = Path(__file__).resolve().parent / 'code'
sys.path.append(str(path))
# Módulos externos
from functions import Jogo

jogo = Jogo()
jogo.escolher_cor()
jogo.jogar()