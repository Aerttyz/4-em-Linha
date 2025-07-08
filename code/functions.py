class Jogo:
  
  def __init__(self):
    # Representa o ambiente do jogo '4 linhas', o qual, em geral, possui 6 linhas e 7 colunas
    self.grid = [['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '']]
    self.cor_X = 'X'
    self.cor_O = 'O'

  def player(self, grid: list, cor: str) -> None:
      posicao = int(input())
      if posicao >= 0 and posicao <= 6:
          linha = self.vefificar_tabuleiro(grid, posicao)
          if linha != -1:
              grid[linha][posicao] = cor
          else:
              print('Jogada inválida')
      else:
          print('Jogada inválida')

  def player_IA(self) -> None:
      pass

  def alternar_cor(self, cor: str) -> str:
      if self.cor_X == cor:
        return self.cor_O
      else:
        return self.cor_X

  def vefificar_tabuleiro(self, pos) -> int:
    for linha in reversed(range(len(self.grid))):
      if self.grid[linha][pos] == '':
        return linha
    return -1

  def exibir_tabuleiro(self) -> None:
     for x, y in enumerate(self.grid):
        print(y)

  def jogar(self) -> None:
    cor = self.cor_X
    while True:
        cor = self.alternar_cor(cor)
        print(f'Vez do jogador {cor}')
        self.vefificar_tabuleiro()
        self.player(self.grid, cor)
        self.vefificar_tabuleiro()

  def verificar_vitoria(self, grid: list, cor) -> bool:
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

  def estima_sucesso(self) -> list:
    
    matriz_sucesso_horizontal = []
    contador = 4
    for coluna in range(7):
      for linha in range(5, -1, -1):
           if self.grid[linha][coluna] != '':
              continue
           else:
              if self.grid[linha+1][coluna] == self.cor_O:
                  linha_atual = linha
                  linha_atual += 1
                  while linha_atual != 6 and self.grid[linha_atual][coluna] == self.cor_O:
                    contador -= 1
                    linha_atual += 1
                  matriz_sucesso_horizontal.append(contador)

    return matriz_sucesso_horizontal
              
              
              
        

