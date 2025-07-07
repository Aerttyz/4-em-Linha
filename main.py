# Representa o ambiente do jogo '4 linhas', o qual, em geral, possui 6 linhas e 7 colunas
grid = [['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '']]
cor = 'X' 

def player(grid: list, cor):
  posicao = int(input())
  if posicao>=0 and posicao<=6:
    linha = vefificar_tabuleiro(grid, posicao)
    if linha != -1:
      grid[linha][posicao] = cor
    else:
      print('Jogada inválida')
  else:
    print('Jogada inválida')

def player_IA(grid: list):
  pass

def alternar_cor():
  global cor
  if cor == 'X':
    cor = 'O'
    return 'O'
  else:
    cor = 'X'
    return 'X'

def vefificar_tabuleiro(grid: list, pos):
  for linha in reversed(range(len(grid))):
    if grid[linha][pos] == '':
      return linha
  return -1

def jogar():
  while True:
      cor = alternar_cor()
      print(f'Vez do jogador {cor}')
      player(grid, cor)
      print(grid)

def verificar_vitoria(grid: list, cor):
  #horizontal 
  for linha in range(6):
    for coluna in range(4):
      if all(grid[linha][coluna+i] == cor for i in range(4)):
        return True
  
  #vertical
  for linha in range(3):
    for coluna in range(7):
      if all(grid[linha+i][coluna] == cor for i in range(4)):
        return True

  #diagonal pra cima
  for linha in range(3):
    for coluna in range(4):
      if all(grid[linha+i][coluna+i] == cor for i in range(4)):
        return True

  #diagonal pra baixo
  for linha in range(3, 6):
    for coluna in range(4):
      if all(grid[linha-i][coluna+i] == cor for i in range(4)):
        return True

  return False

jogar()