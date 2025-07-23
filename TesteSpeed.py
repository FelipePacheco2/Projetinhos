import time 

# Função de Pesquisa Binária
def pesquisa_binaria(lista, valor):
    """
    Realiza uma busca binária para encontrar o índice de um valor na lista.
    A lista deve estar ordenada.
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == valor:
            return meio  # Valor encontrado
        elif chute > valor:
            alto = meio - 1  # Valor está na metade inferior
        else:
            baixo = meio + 1  # Valor está na metade superior

    return None  # Valor não encontrado


# Função de Pesquisa Simples (Linear)
def pesquisa_simples(lista, valor):
    """
    Realiza uma busca simples (linear) para encontrar o valor na lista.
    """
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None


# Lista com 1 milhão de elementos
lista_numeros = list(range(1, 1000001))
valor_procurado = 824000


# -----------------------
# Tempo da Pesquisa Binária
# -----------------------
inicio_binaria = time.time()
pesquisa_binaria(lista_numeros, valor_procurado)
fim_binaria = time.time()
tempo_binaria = fim_binaria - inicio_binaria


# -----------------------
# Tempo da Pesquisa Simples
# -----------------------
inicio_simples = time.time()
pesquisa_simples(lista_numeros, valor_procurado)
fim_simples = time.time()
tempo_simples = fim_simples - inicio_simples


# -----------------------
# Resultados
# -----------------------
print("\n=== COMPARAÇÃO DE TEMPOS DE EXECUÇÃO ===")
print(f"Tempo de execução (Pesquisa Binária): {tempo_binaria:.4f} segundos")
print(f"Tempo de execução (Pesquisa Simples): {tempo_simples:.4f} segundos")

print("\nEste código compara dois métodos de busca para encontrar um número específico em uma lista de 1 milhão de elementos.")
print("A pesquisa binária é muito mais eficiente para listas ordenadas, pois divide o problema pela metade a cada passo.")
print("Já a pesquisa simples verifica elemento por elemento até encontrar o valor desejado.\n")