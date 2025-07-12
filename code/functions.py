class Jogo:
  
  def __init__(self):
    # Representa o ambiente do jogo '4 linhas', o qual, em geral, possui 6 linhas e 7 colunas
    self.grid = [['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '']]
    self.cor_player = 'X'
    self.cor_cpu = 'O'

  def escolher_cor(self) -> None:
    while True:
        cor_escolhida = input("Escolha sua cor (X ou O): ").strip().upper()
        if cor_escolhida in ['X', 'O']:
            self.cor_player = cor_escolhida
            self.cor_cpu = 'O' if cor_escolhida == 'X' else 'X'
            print(f"Você escolheu: {self.cor_player}. A IA será: {self.cor_cpu}.")
            break
        else:
            print("Escolha inválida. Digite X ou O.")

  def player(self, cor: str) -> None:
      posicao = int(input())
      if posicao >= 0 and posicao <= 6:
          linha = self.vefificar_tabuleiro(posicao)
          if linha != -1:
              self.grid[linha][posicao] = cor
          else:
              print('Jogada inválida')
      else:
          print('Jogada inválida')

  def player_IA(self) -> None:
      posicao = self.escolher_melhor_jogada()
      if posicao >= 0 and posicao <= 6:
          linha = self.vefificar_tabuleiro(posicao)
          if linha != -1:
              self.grid[linha][posicao] = self.cor_cpu
          else:
              print('Jogada inválida')
      else:
          print('Jogada inválida')

  def alternar_cor(self, cor: str) -> str:
      return self.cor_cpu if cor == self.cor_player else self.cor_player

  def vefificar_tabuleiro(self, posicao: int) -> int:
    for linha in reversed(range(len(self.grid))):
      if self.grid[linha][posicao] == '':
        return linha
    return -1

  def exibir_tabuleiro(self) -> None:
     for x, y in enumerate(self.grid):
        print(y)

  def jogar(self) -> None:

    while True:
      self.exibir_tabuleiro()
      print(f'Vez do jogador {self.cor_player}')
      self.player(self.cor_player)
      if self.verificar_vitoria(self.cor_player):
        self.exibir_tabuleiro()
        print(f'Jogador {self.cor_player} venceu!')
        break

      self.exibir_tabuleiro()
      print(f'Vez do jogador {self.cor_cpu}')
      self.player_IA()
      if self.verificar_vitoria(self.cor_cpu):
        self.exibir_tabuleiro()
        print(f'A IA ({self.cor_cpu}) venceu!')
        break


  def verificar_vitoria(self, cor: str) -> bool:
    #horizontal 
    for linha in range(6):
      for coluna in range(4):
        if all(self.grid[linha][coluna+i] == cor for i in range(4)):
          return True
    
    #vertical
    for linha in range(3):
      for coluna in range(7):
        if all(self.grid[linha+i][coluna] == cor for i in range(4)):
          return True

    #diagonal pra cima
    for linha in range(3):
      for coluna in range(4):
        if all(self.grid[linha+i][coluna+i] == cor for i in range(4)):
          return True

    #diagonal pra baixo
    for linha in range(3, 6):
      for coluna in range(4):
        if all(self.grid[linha-i][coluna+i] == cor for i in range(4)):
          return True

    return False

  def avaliar_vertical(self, coluna: int) -> int:
    score_coluna = 0
    for linha in range(3):
      trecho = [self.grid[linha + i][coluna] for i in range(4)]
      n_cpu = trecho.count(self.cor_cpu)
      n_vazias = trecho.count('')
      if n_cpu > 0 and n_cpu + n_vazias == 4:
        score_coluna += n_cpu * 10
      elif n_cpu + n_vazias < 4:
        score_coluna -= 100
    return score_coluna

  def avaliar_horizontal(self, linha: int) -> int:
    score_linha = 0
    for coluna in range(4):
      trecho = [self.grid[linha][coluna + i] for i in range(1, 4)]
      trecho += [self.grid[linha][coluna - i] for i in range(1, 4)]
      n_cpu = trecho.count(self.cor_cpu)
      n_vazias = trecho.count('')
      if n_cpu > 0 and n_cpu + n_vazias == 4:
        score_linha += n_cpu * 10
      elif n_cpu + n_vazias < 4:
        score_linha -= 100
    return score_linha
  
  def avaliar_diagonais(self) -> int:
    score_diagonal = 0

    for linha in range(3):
      for coluna in range(4):
        trecho = [self.grid[linha + i][coluna + i] for i in range(4)]
        n_cpu = trecho.count(self.cor_cpu)
        n_vazias = trecho.count('')
        if n_cpu > 0 and n_cpu + n_vazias == 4:
            score_diagonal += n_cpu * 10
        elif n_cpu + n_vazias < 4:
            score_diagonal -= 100

    for linha in range(3):
      for coluna in range(3, 7):
        trecho = [self.grid[linha + i][coluna - i] for i in range(4)]
        n_cpu = trecho.count(self.cor_cpu)
        n_vazias = trecho.count('')
        if n_cpu > 0 and n_cpu + n_vazias == 4:
            score_diagonal += n_cpu * 10
        elif n_cpu + n_vazias < 4:
            score_diagonal -= 100

    for linha in range(3, 6):
      for coluna in range(4):
        trecho = [self.grid[linha - i][coluna + i] for i in range(4)]
        n_cpu = trecho.count(self.cor_cpu)
        n_vazias = trecho.count('')
        if n_cpu > 0 and n_cpu + n_vazias == 4:
            score_diagonal += n_cpu * 10
        elif n_cpu + n_vazias < 4:
            score_diagonal -= 100

    for linha in range(3, 6):
      for coluna in range(3, 7):
        trecho = [self.grid[linha - i][coluna - i] for i in range(4)]
        n_cpu = trecho.count(self.cor_cpu)
        n_vazias = trecho.count('')
        if n_cpu > 0 and n_cpu + n_vazias == 4:
            score_diagonal += n_cpu * 10
        elif n_cpu + n_vazias < 4:
            score_diagonal -= 100

    return score_diagonal

  
  def escolher_melhor_jogada(self) -> int:
    melhor_score = float('-inf')
    melhor_coluna = None

    for coluna in range(7):
        linha = self.vefificar_tabuleiro(coluna)
        if linha == -1:
            continue

        self.grid[linha][coluna] = self.cor_cpu

        score_vertical = self.avaliar_vertical(coluna)
        score_horizontal = self.avaliar_horizontal(linha)
        score_diagonais = self.avaliar_diagonais()

        score_total = score_vertical + score_horizontal + score_diagonais

        self.grid[linha][coluna] = ''

        if score_total > melhor_score:
            melhor_score = score_total
            melhor_coluna = coluna

    return melhor_coluna


      






   
              
              
              
        

