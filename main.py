# Módulos nativos
import os
import sys

# Paths (insira o seu logo abaixo)
sys.path.append('/home/fulano/Documentos/4-em-Linha/code')
# Módulos externos
from functions import Jogo

jogo = Jogo()
jogo.escolher_cor()
jogo.jogar()