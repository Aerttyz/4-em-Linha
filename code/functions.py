from typing import Optional, Tuple
class Jogo:
  
  def __init__(self):
    """
    Inicializa os atributos (grid e cores dos jogadores) de uma instância da classe Jogo
    """
    self.grid = [['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '']]
    self.cor_player = 'X'
    self.cor_cpu = 'O'

  def escolher_cor(self) -> None:
    """
    Solicita que o player escolha a cor que preencherá os espaços do grid em suas jogadas. Define a cor restante para
    a CPU.
    """

    while True:
        cor_escolhida = input("Escolha sua cor (X = 🟡 ou O = 🔴): ").strip().upper()
        if cor_escolhida in ['X', 'O']:
            self.cor_player = cor_escolhida
            self.cor_cpu = 'O' if cor_escolhida == 'X' else 'X'
            print(f"Você escolheu: {self.cor_player}. A IA será: {self.cor_cpu}.")
            break
        else:
            print("Escolha inválida. Digite X ou O.")

  def player(self, cor: str) -> None:
      """
      Enquanto uma jogada válida não for efetuada pelo player:
      Recebe o índice de uma coluna informada pelo player. Em seguida, verifica se o índice da coluna está no intervalo (inclusivo)
      compreendido entre 0 e 6. Caso pertença ao intervalo, retorna o índice da linha com base na disposição do preenchimento das
      células do grid, e preenche a célula indexada aos respectivos componentes (linha x coluna) com a cor escolhida pelo player.
      Caso não pertença ou caso a coluna já esteja preenchida até o topo, o player é informado que a jogada é inválida.
      """
      jogada_efetuada = False
      while not jogada_efetuada:
        posicao = int(input("Player, em qual coluna você deseja efetuar a jogada? (Valores possíveis: 1 ~ 7): "))
        posicao -= 1
        if posicao >= 0 and posicao <= 6:
            linha = self.verificar_tabuleiro(posicao)
            if linha != -1:
                self.grid[linha][posicao] = cor
                jogada_efetuada = True
                break
            else:
                print('Jogada inválida')
        else:
            print('Jogada inválida')

  def player_IA(self) -> None:
      """
      Modulariza função que preenche a célula associada à coluna escolhida pela CPU.

      Primeiro, a IA irá calcular qual coluna maximizará sua jogada. Em seguida, o
      índice da coluna será retornado, bem como a linha disponível associada à refe-
      rida coluna, com o objetivo de preencher com a cor do jogador 'CPU' a célula 
      indexada aos elementos retornados.

      Além disso, adiciona camada extra de verificação acerca dos índices escolhidos
      para que a CPU não efetue uma jogada inválida. Enquanto a jogada não for válida,
      a CPU retornará para a etapa de seleção da melhor jogada.
      """
      
      profundidade = 4  
      _, posicao = self.minimax_alpha_beta(profundidade, True, float('-inf'), float('inf'))

      jogada_efetuada = False
      while not jogada_efetuada:
        if posicao >= 0 and posicao <= 6:
            linha = self.verificar_tabuleiro(posicao)
            if linha != -1:
                self.grid[linha][posicao] = self.cor_cpu
                jogada_efetuada = True
                break
            else:
                print('Jogada inválida')
        else:
            print('Jogada inválida')

  def verificar_tabuleiro(self, posicao: int) -> int:
    """
    Retorna o índice da linha associada ao índice
    da coluna cuja célula está vazia.

    Parâmetros:
      posicao: int -> Representa o índice da coluna

    Retorno:
      int: representa o índice da referida linha
    """
    for linha in reversed(range(len(self.grid))):
      if self.grid[linha][posicao] == '':
        return linha
    return -1

  def exibir_tabuleiro(self) -> None:
     """
     Imprime a disposição do grid por meio da iteração
     pelos valores (espaços) do tabuleiro.
     """
     print(" 1  2  3  4  5  6  7")
     for linha in self.grid:
        for celula in linha:
            if celula == 'X':
                print("🟡", end=' ')
            elif celula == 'O':
                print("🔴", end=' ')
            else:
                print("⚪", end=' ')
        print()

  def jogar(self) -> None:
    """
    Função principal responsável por agregar tanto a chamada da função do player e da CPU
    quanto a verificação de ocorrência de vitórias após cada jogada, bem como por exibir
    o grid (tabuleiro) após cada jogada.
    """

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
    """
    Função responsável por verificar se houve uma sequência de 4 células preenchidas
    pela cor passada como parâmetro nas direções horizontal, vertical, diagonal para
    cima e diagonal para baixo. Caso a ocorrência seja verdadeira, retorna True. Caso
    contrário, retorna False

    Parâmetros:
      cor: str -> Corresponde à cor do player ou da CPU ('X' ou 'O')

    Retorno:
      bool: corresponde a evidência de ocorrência ou não ocorrência de vitória por algum
      dos jogadores.
    """
    
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
    """
    Função responsável por estimar a pontuação na direção vertical, com base na 
    coluna passada como parâmetro. Por exemplo: quanto maior for a quantidade de
    células preenchidas na vertical em determinada coluna, maior será a estimativa
    da pontuação, tendo em vista que a CPU estará mais próximo da vitória.

    Nesse sentido, a heurística da estimativa na direção vertical foi implementada
    da seguinte maneira: 

    1) Declara-se e atribui o valor '0' à variável 'score_coluna';

    2) Para cada linha no range(3), isto é, para as linhas com índice 0, 1 e 2:

      2.1) Por meio de um 'list comprehension', armazena-se em uma lista uma sequência de
          4 células indexadas à coluna passada como parâmetro e às linhas acrescidas com
          o valor 'i' no range(4), isto é, no intervalo de valores de 0, 1, 2 e 3, tendo
          como referência o índice atual da linha definido na etapa 2).

      2.2) Verifica-se, para cada sequência, quantas células estão preenchidas com a cor
          da CPU (valor armazenado na variável 'n_cpu');

      2.3) Verifica-se, para cada sequência, quantas células não estão preenchidas (valor
          armazenado na variável 'n_vazias').

      2.4) Verifica se o valor calculado em 2.2) é maior que zero e se a soma dos valores
          calculados em 2.2) e em 2.3) corresponde a 4.

      2.5) Em caso afirmativo, o score da coluna é acrescido de 10*(quantidade de células
          preenchidas com a cor da CPU).

      2.6) Caso seja inferior a 4, o score associado ao índice da coluna é penalizado,
          sendo subtraído 100 unidades de seu valor.

    3) Ao fim das iterações, o score (pontuação) da coluna é retornado, na perspectiva
        de análise da maximização na direção vertical.

    Parâmetros:
      coluna: int -> Corresponde à posição/índice da coluna 
    
    Retorno:
      int: corresponde à pontuação estimada da coluna na perspectiva de análise da maximização
          na direção vertical.

    """

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
    """
    Função responsável por estimar a pontuação na direção horizontal, com base na 
    linha passada como parâmetro. Por exemplo: quanto maior for a quantidade de
    células preenchidas na horizontal tendo como base a célula que pode ser preenchida
    a partir de determinada coluna como índice, maior será a estimativa da pontuação, 
    tendo em vista que a CPU estará mais próximo da vitória.

    Nesse sentido, a heurística da estimativa na direção horizontal foi implementada
    da seguinte maneira: 

    1) Declara-se e atribui o valor '0' à variável 'score_linha';

    2) Para cada coluna no range(4), isto é, para as colunas com índice 0, 1, 2 e 3:

      2.1) Por meio de um 'list comprehension', armazena-se em uma lista uma sequência de
          3 células indexadas à linha passada como parâmetro e às colunas acrescidas e
          decrementadas com o valor 'i' no range(1, 4), isto é, no intervalo de valores de
          1, 2 e 3, tendo como referência o índice atual da linha definido na etapa 2).

          Na prática, analisa-se as três células anteriores e as três células sucessoras.

      2.2) Verifica-se na sequência, quantas células estão preenchidas com a cor da CPU 
          (valor armazenado na variável 'n_cpu');

      2.3) Verifica-se na sequência, quantas células não estão preenchidas (valor armazenado
          na variável 'n_vazias').

      2.4) Verifica se o valor calculado em 2.2) é maior que zero e se a soma dos valores
          calculados em 2.2) e em 2.3) corresponde a 4.

      2.5) Em caso afirmativo, o score da linha é acrescido de 10*(quantidade de células
          preenchidas com a cor da CPU).

      2.6) Caso seja inferior a 4, o score associado ao índice da linha é penalizado,
          sendo subtraído 100 unidades de seu valor.

    3) Ao fim das iterações, o score (pontuação) da linha é retornado, na perspectiva
        de análise da maximização na direção horizontal.

    Parâmetros:
      coluna: int -> Corresponde à posição/índice da linha 
    
    Retorno:
      int: corresponde à pontuação estimada da coluna na perspectiva de análise da maximização
          na direção horizontal.

    """

    score_linha = 0
    for coluna in range(4):
      trecho = [self.grid[linha][coluna + i] for i in range(4)]
      n_cpu = trecho.count(self.cor_cpu)
      n_vazias = trecho.count('')
      if n_cpu > 0 and n_cpu + n_vazias == 4:
        score_linha += n_cpu * 10
      elif n_cpu + n_vazias < 4:
        score_linha -= 100
    return score_linha
  
  def avaliar_diagonais(self, linha: int, coluna: int) -> int:
    """
    Função responsável por estimar a pontuação na direção das diagonais. Por exemplo: 
    quanto maior for a quantidade de células preenchidas em cada diagonal (superior
    esquerda, superior direita, inferior esquerda e inferior direta), maior será a
    estimativa da pontuação, tendo em vista que a CPU estará mais próximo da vitória.

    Nesse sentido, a heurística da estimativa na direção diagonal foi implementada
    da seguinte maneira: 

    1) Declara-se e atribui o valor '0' à variável 'score_diagonal';

    2) Declara-se a variável 'direções' (correspondente a uma lista de tuplas cujos valores
        equivalem a pares ordenados x, y, isto é, índices de linha e coluna associados a
        todos os sentidos da direção diagonal);

    3) Itera por cada tupla da lista (isto é, cada diagonal da referida célula será analisada):

      3.1) Declara-se a variável trecho e a inicializa com uma lista vazia;

      3.2) Declara-se a variável contador e a inicializa com o valor '1';

      3.3) Enquanto o valor do contador for inferior à 4:

        3.3.1) Enquanto a célula na diagonal averiguada: a) possuir um valor diferente da cor do oponente;
              b) possuir um índice válido, existente no grid do jogo; adicione tal célula à variável 'trecho'.
              
        3.3.2) Caso contrário, o 'while' loop é interrompido e a próxima diagonal é analisada.

    4) Ao fim, calcula-se, com base na quantidade de células vazias e preenchidas com a cor da CPU nas respectivas
        diagonais, o valor estimado na direção diagonal da pontuação ao jogar na referida coordenada repassada como
        parâmetro.
    
    5) Por fim, a pontuação supramencionada é retornada.

    Parâmetros:
      linha: int -> corresponde ao índice da linha associada à célula disponível na respectiva coluna
      coluna: int -> corresponde ao índice da coluna analisada pela CPU
    
    Retorno:
      int: corresponde à pontuação estimada da coluna na perspectiva de análise da maximização
          na direção diagonal.

    """

    score_diagonal = 0
    direcoes = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    for dx, dy in direcoes:
      trecho = []
      contador = 1
      while contador < 4:
        nova_linha = linha + dx * contador
        nova_coluna = coluna + dy * contador
        if 0 <= nova_linha < 6 and 0 <= nova_coluna < 7:
          if self.grid[nova_linha][nova_coluna] == self.cor_player:
            break
          trecho.append(self.grid[nova_linha][nova_coluna])
        else:
            break
        contador += 1
       
    n_cpu = trecho.count(self.cor_cpu)
    n_vazias = trecho.count('')
    if n_cpu > 0 and n_cpu + n_vazias == 4:
      score_diagonal += n_cpu * 10
    elif n_cpu + n_vazias < 4:
      score_diagonal -= 100

    return score_diagonal

  def avaliar_tabuleiro(self) -> int:
    """
    Avalia o tabuleiro e retorna a pontuação total com base nas heurísticas de avaliação
    vertical, horizontal e diagonal.

    Retorno:
      int: pontuação total do tabuleiro.
    """
    score_total = 0
    for linha in range(6):
        for coluna in range(7):
            if self.grid[linha][coluna] == self.cor_cpu:
                score_total += self.avaliar_vertical(coluna)
                score_total += self.avaliar_horizontal(linha)
                score_total += self.avaliar_diagonais(linha, coluna)
            elif self.grid[linha][coluna] == self.cor_player:
                score_total -= (self.avaliar_vertical(coluna) +
                                self.avaliar_horizontal(linha) +
                                self.avaliar_diagonais(linha, coluna))
    return score_total

  def minimax_alpha_beta(self, profundidade: int, max: bool, alfa: float, beta: float) -> Tuple[int, Optional[int]]:
    """
    Implementa o algoritmo Minimax com poda Alpha-Beta para determinar a melhor jogada da CPU.
    
    Retorno:
      Tuple[int, Optional[int]]: Retorna a pontuação da melhor jogada e o índice da coluna escolhida.
    """
    if self.verificar_vitoria(self.cor_cpu):
        return 1000, None
    elif self.verificar_vitoria(self.cor_player):
        return -1000, None
    elif profundidade == 0:
        return self.avaliar_tabuleiro(), None
    
    if max:
        return self.maximizar(profundidade, alfa, beta)
    else:
        return self.minimizar(profundidade, alfa, beta)
    
  def maximizar(self, profundidade: int, alfa: float, beta: float) -> Tuple[int, Optional[int]]:
    """
    Maximiza a pontuação da CPU, escolhendo a melhor coluna para jogar.
    Retorno:
      Tuple[int, Optional[int]]: Retorna a pontuação máxima e o índice da coluna escolhida.
    """

    melhor_score = float('-inf')
    melhor_coluna = None

    for coluna in range(7):
        linha = self.verificar_tabuleiro(coluna)
        if linha == -1:
            continue

        self.grid[linha][coluna] = self.cor_cpu
        score, _ = self.minimax_alpha_beta(profundidade - 1, False, alfa, beta)
        self.grid[linha][coluna] = ''

        if score > melhor_score:
            melhor_score = score
            melhor_coluna = coluna
        alfa = max(alfa, score)
        if beta <= alfa:
            break

    return melhor_score, melhor_coluna
  
  def minimizar(self, profundidade: int, alfa: float, beta: float) -> Tuple[int, Optional[int]]:
    menor_score = float('inf')
    melhor_coluna = None

    for coluna in range(7):
        linha = self.verificar_tabuleiro(coluna)
        if linha == -1:
            continue

        self.grid[linha][coluna] = self.cor_player
        score, _ = self.minimax_alpha_beta(profundidade - 1, True, alfa, beta)
        self.grid[linha][coluna] = ''

        if score < menor_score:
            menor_score = score
            melhor_coluna = coluna
        beta = min(beta, score)
        if beta <= alfa:
            break
    return menor_score, melhor_coluna
      






   
              
              
              
        

