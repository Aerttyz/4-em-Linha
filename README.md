# 🧠 Decisões Ótimas em Jogos: IA para o "Quatro em Linha"

## 🎯 Objetivos e Aplicações

O objetivo principal deste projeto é implementar um agente inteligente capaz de jogar o jogo "Quatro em Linha" contra um jogador humano. A ideia é simular uma IA que:

- Avalia o estado atual do jogo;
- Prevê as melhores jogadas possíveis;
- Evita derrotas e maximiza chances de vitória;
- Compete com um oponente humano em tempo real.

**Aplicações práticas:**
- Desenvolvimento de jogos com inteligência artificial básica;
- Aplicação de técnicas de busca e heurística em ambientes determinísticos e de soma zero;
- Estudo e prática de conceitos de Inteligência Artificial aplicados a jogos.

---

## 🧮 Algoritmos e Modelagem da IA

### 🔍 Métodos de IA Utilizados

- **Heurística personalizada**: cálculo de pontuação baseado em padrões no tabuleiro (horizontal, vertical e diagonais).
- **Minimax com poda Alfa-Beta** (planejado para futura expansão): utilizado para analisar cenários mais profundos e evitar caminhos ruins sem explorar todas as possibilidades.

### 🔠 Representação de Conhecimento

O conhecimento é representado como um grid `6x7`, onde cada célula contém `'X'`, `'O'` ou `''`. A IA analisa o estado atual do tabuleiro e simula jogadas futuras para tomar decisões.

---

## 🧱 Modelagem PEAS

| **Componente**      | **Descrição**                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| **P** (Performance) | Número de vitórias, jogadas defensivas bem-sucedidas, e decisões vantajosas. |
| **E** (Environment) | Tabuleiro 6x7, regras do jogo, ações do oponente.                             |
| **A** (Actuators)   | Jogar uma peça em uma coluna válida.                                          |
| **S** (Sensors)     | Estado atual do tabuleiro e jogadas do oponente.                             |

---

## 🧠 Arquitetura do Agente

O agente segue a arquitetura de **agente baseado em objetivos com heurísticas**, que:

1. Analisa o estado atual (sensores);
2. Simula jogadas válidas;
3. Avalia com funções heurísticas (pontuação das jogadas);
4. Executa a jogada com maior pontuação estimada (atuadores).

> Apesar de não utilizar o Minimax completo neste momento, a estrutura de heurísticas permite simular parcialmente o comportamento preditivo da IA.

---

## 📏 Métricas, Testes e Validação

### 🧪 Métricas Utilizadas

- **Número de derrotas evitadas**;
- **Vitórias diretas não ignoradas**;
- **Capacidade de prever jogadas perigosas**.

### ✅ Metodologia de Validação

- Testes manuais observando partidas reais entre jogadores e a IA;
- Casos como "a IA ignorar vitória iminente" ou "não defender contra derrota iminente" foram usados para refinar as heurísticas;
- Ajustes sucessivos foram feitos até a IA tomar decisões mais robustas.

---

## ⚠️ Limitações e Dificuldades

### 🧩 Dificuldades Técnicas

- Construção e validação das heurísticas;
- Ajuste da profundidade ideal para análise (hoje definida como 4);
- Testes manuais demorados, sem automação.

### 🚧 Limitações Atuais

- A IA não prevê mais de uma jogada à frente de forma efetiva;
- Heurísticas são locais e imediatistas;
- Não há camadas de dificuldade configuráveis.

---

## 💡 Sugestões de Melhorias

1. **Implementar Minimax com poda Alfa-Beta completa**:
   - Analisar profundidades maiores com menos custo computacional;
   - Tomada de decisões mais estratégicas.

2. **Adicionar diferentes níveis de dificuldade**:
   - Fácil (aleatório ou heurística básica);
   - Médio (heurística refinada);
   - Difícil (Minimax com profundidade adaptativa).

3. **Implementar testes automatizados**:
   - Garantir que a IA tome decisões corretas em todos os estados do jogo.

4. **Interface gráfica**:
   - Tornar a experiência mais acessível via Pygame ou Tkinter.

5. **Sistema de logs**:
   - Armazenar cada jogada e o motivo da escolha da IA para análise futura.

---

## 📎 Conclusão

Este projeto é um excelente exemplo de aplicação prática de conceitos fundamentais da IA em um problema de jogo determinístico e competitivo. Apesar das limitações, a modelagem heurística implementada já permite que o agente tome decisões razoavelmente inteligentes. Com algumas melhorias (como a introdução de Minimax completo e testes automatizados), o projeto pode ser transformado em uma plataforma de experimentação mais robusta e até servir de base para ensino de IA em jogos.

---
