import numpy as np

mapa = np.random.randint(0, 10, size=(5, 5)) #criando matrix 5x5 de numeros aleatorios

while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0): # Caso o tesouro caia na posição 0
        break

posicao_jogador = (0, 0)
pontuacao = 0

def mostra_map(mapa, posicao_jogador): # Manipulação do mapa (copia)
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1

    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador)
    mapa_com_jogador_str[mapa_com_jogador == -1] = ' X'

    print('\nMapa Novo')
    for linha in mapa_com_jogador_str:
        print(' '.join(linha))

while True:     # movimentação do personagem
    mostra_map(mapa, posicao_jogador)

    direcao = input("Infomarme a direção que deseja mover? (Cima, Baixo, Direita, Esquerda) :").strip().lower()
    movimentos = {
        'cima': (-1, 0),
        'baixo': (1, 0),
        'direira': (0, 1),
        'esquerda': (0, -1),
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1),
    }

    if direcao in movimentos:
        nova_posicao = (
            posicao_jogador[0] + movimentos[direcao][0], 
            posicao_jogador[1] + movimentos[direcao][1]
        )
        
        if (0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] < mapa.shape[1]):  # vericando se posição é valida
            posicao_jogador = nova_posicao                          
            pontuacao += 1
        else:
            print("Movimento Fora dos Limites! Tente Novamente")
    else:
        print('Direção Invalida! Tente Novamente')

    if posicao_jogador == (tesouro_linha, tesouro_coluna):  # Se encotrar o tesouro
        mostra_map(mapa, posicao_jogador)
        print("\n\n=====Você acho o tesouro=====")
        print(f"Pontuação final : {pontuacao}")
        print(f"O tesoura estava na posiçao {(int(tesouro_linha), (tesouro_coluna))}")
        break