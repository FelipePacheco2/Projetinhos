import pandas as pd

Cliente = {
    'Nome' : [],
    'Telefone' : [],
    'Situação' : []
}


def cadastro():
    while True:
        print("==== Cadastro ====")
        try:
            name = str(input("Digite nome do cliente :")).strip().lower()
            telefone = int(input("Digite o telefone (apenas números): "))
        except ValueError:
            print("Dados digitados errados. Tente novamente.")
            continue

        try:
            switch = int(input("[1] Alto\n"
                               "[2] Baixo\n" 
                               "[3] Neutro\n" 
                               "Escolha: "))
        except ValueError:
            print("Opção inválida! Situação não registrada.")
            continue

        Cliente["Nome"].append(name)
        Cliente["Telefone"].append(telefone)

        if switch == 1:
            Cliente["Situação"].append('Alto')
        elif switch == 2:
            Cliente["Situação"].append('Baixo')
        elif switch == 3:
            Cliente['Situação'].append('Neutro')
        else:
            print("Opçao Invalidade")
            continue

        continuar = int(input("[1] Novo Cadastro\n" 
                              "[2] Sair\n" 
                              "Escolha: "))
        if continuar == 2:
            break

def lista_clinte():
    if not Cliente['Nome']:
        print("Nenhum Cliente Cadastrado ")
    else:
        df_cliente = pd.DataFrame(Cliente)
        df_cliente.index = range(1, len(df_cliente) + 1)
        return print(df_cliente)

def Editar():
    print("==== Editar Cliente ====")
    lista_clinte()
    idx = int(input("Digite indice do cliente"))

switch = 0
while switch != 4:
    print('==== Painel CRM ====\n')
    switch = int(input("[1] Cadastro\n"
                       "[2] Listar Clientes\n"
                       "[3] Editar Cliente\n"
                       "[4] sair\n"
                       "Escolha: "))
    if switch == 1:
       cadastro()
    elif switch == 2:
        lista_clinte()
    elif switch == 3:
        Editar()
    elif switch == 4:
        print("Programa Finalizado")
    else:
        print("Opçao Invaldiade")  
