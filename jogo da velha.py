import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):   # colocando a peça do jogador na pociçao escolhida
    tabuleiro[linha][coluna] = peca
    
def verificar_vitoria(tabuleiro, peca): # verificando se o jogador ganhou
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    coluna = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    return linhas or coluna or diagonais

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(str(x) if x != 0 else ' ' for x in linha))
        print("=" * 8)

def game(): #funçao principal 
    tabuleiro = np.zeros((3,3), dtype=int)

    peca_atual = 1
    vencedor = False
    empate = False 

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)

        while True:
            try:
                linha = int(input(f"Jogador {peca_atual}, escolha a linha (0, 1, 2): "))
                coluna = int(input(f"Jogador {peca_atual}, escolha a coluna (0, 1, 2): "))

                if linha not in [0, 1, 2] or coluna not in [0, 1, 2]: # validando dados 
                    print("\nEscolha linhas e colunas válida! 0 a 2\n")
                    continue

                if tabuleiro[linha][coluna] != 0: # verificar se esta ocupada
                    print("\nPosição ocupada! Tente Novamente")
                    continue

                colocar_peca(tabuleiro, linha, coluna, peca_atual)
                vencedor = verificar_vitoria(tabuleiro, peca_atual) 

                if np.all(tabuleiro != 0):
                    empate = True
                break

            except IndexError:
                print("\nEntrada inválida! Por favor insira numeros inteiros entre 0 a 2")
            
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    if vencedor:
        print(f"\n\tParabens Você venceu o jogo")
    else:
        print(f"\nEmpate")

game()