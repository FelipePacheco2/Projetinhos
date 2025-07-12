import pandas as pd

caminho_filmes = "Analises-de-filmes-do-IMBD/datasets/imdb_list.csv"
df_filmes = pd.read_csv(caminho_filmes, sep=",", decimal=".")

def Best_filme():
    print("Melhores filmes do IMDB:\n")
    print("[1] Listar filmes com maior nota")
    print("[2] Listar filmes com menor nota")
    print("[0] Sair")

    escolha = int(input("Escolha uma opção: "))
    qts_filmes = int(input("Quantos filmes você quer ver?"))

    if escolha == 1:
        print("Filmes com maior nota:")
        maior_nota = df_filmes[df_filmes["rating"] <= df_filmes["rating"].max()].sort_values(by="rating", ascending=False)
        df_maior_nota = pd.DataFrame(maior_nota[["title", "year", "rating", "genre"]].head(qts_filmes).reset_index(drop=True))
        df_maior_nota.index += 1
        print(df_maior_nota)
    elif escolha == 2:
        print("Filmes com menor nota:")
        menor_nota = df_filmes[df_filmes["rating"] >= df_filmes["rating"].min()].sort_values(by="rating", ascending=True)
        df_menor_nota = pd.DataFrame(menor_nota[["title", "year", "rating", "genre"]].head(qts_filmes).reset_index(drop=True))
        df_menor_nota.index += 1
        print(df_menor_nota)
    elif escolha == 0:
        print("Saindo...")
        return 
    else:
        print("Opção inválida. Tente novamente.")
        return

def Best_genero():
    print("Melhores filmes por gênero:")
    genero = df_filmes["genre"].dropna().str.split(",").explode().str.strip().unique() 

    for i, x in enumerate(genero):  
        print(f"{i} {x}")
    print("\n")

    try: 
        escolha = int(input("Escolha um gênero: "))
        print(f"Você escolheu o gênero: {genero[escolha]}")
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    filmes_genero = df_filmes[df_filmes["genre"].str.contains(genero[escolha], na=False)] 

    print("[1] Listar filmes")
    print("[2] Listar filmes com maior nota")
    print("[3] Listar filmes com menor nota")
    print("[0] Sair")
        
    escolha_opcao = int(input("Escolha uma opção: "))
    qts_filmes = int(input("Quantos filmes você quer ver? "))

    if escolha_opcao == 1:
        print(f"Filmes do gênero {genero[escolha]}:")
        list  = filmes_genero[["title", "year", "rating", "genre"]].to_string(index=False)
        print(f"{list} \n") 
    elif escolha_opcao == 2:
        maior_nota = filmes_genero[filmes_genero["rating"] <= filmes_genero["rating"].max()].sort_values(by="rating", ascending=False)
        print(f"Filmes do gênero {genero[escolha]} com maior nota:")
        df_maior_nota = pd.DataFrame(maior_nota[["title", "year", "rating", "genre"]].head(qts_filmes).reset_index(drop=True))
        df_maior_nota.index += 1
        print(df_maior_nota)
    elif escolha_opcao == 3:
        menor_nota = filmes_genero[filmes_genero["rating"] >= filmes_genero["rating"].min()].sort_values(by="rating", ascending=True)
        df_menor_nota = pd.DataFrame(menor_nota[["title", "year", "rating", "genre"]].head(qts_filmes).reset_index(drop=True))
        df_menor_nota.index += 1
        print(df_menor_nota)
    elif escolha_opcao == 0:
        print("Saindo...")
        return
    else:
        print("Opção inválida. Tente novamente.")
        return

#main 
while True:
    print("Bem-vindo ao sistema de análise de filmes do IMDB!\n")
    print("Escolha uma opção:")

    print("[1] Todos os filmes")
    print("[2] Ver filmes por gênero")
    print("[0] Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        Best_filme()
    elif escolha == 2:
        Best_genero()
    elif escolha == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
