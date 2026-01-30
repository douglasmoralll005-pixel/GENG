import json
sessoes = []
def salvar_arquivo():
    with open("assuntos.json", "w") as arquivo:
        json.dump(sessoes, arquivo, indent=4)
def carregar_arquivo():
    try:
        with open("assuntos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
def adicionar_sessao():
    global sessoes
    assunto = input("Qual nome do assunto deseja registrar: ")
    while True:
        try:
            tempo  = int(input("Qual tempo que para terminar esse assunto"))
        except ValueError:
            print("ERROR COLOCAR APENAS NUMEROS!")
            continue
        if tempo <0 :
            print("NUMERO INVALIDO")
        else:
            break
    while True:
        try:
            dificuldade = int(input("Qual a dificuldade do assunto registrado entre 0 a 5: "))
        except ValueError:
            print("Digitar apenas numero")
            continue
        if dificuldade < 0:
            print("Numero invalido")
        elif dificuldade >5:
            print("numero invalido")
        else:
            break

    salvar = {
        "assunto":assunto,
        "tempo": tempo,
        "dificuldade":dificuldade
    }
    sessoes.append(salvar)
    salvar_arquivo()

def listar_sessoes():
    if len(sessoes) == 0:
        print("SEM SESSOES REGISTRADAS!")
        return
    print("======Sessoes registradas=====")
    for sessao in sessoes:
        print(f"Assunto:{sessao['assunto']}")
        print(f"Dificuldade:{sessao['dificuldade']}")
        print(f"tempo:{sessao['tempo']}")

def menu():
    global sessoes
    sessoes = carregar_arquivo()
    while True:
        print("========Menu das Sessoes==========")
        print("1 - adicionar sessao")
        print("2 - listar sessoes")
        print("0 - sair")
        opcao = input("ESCOLHA UMA OPCAO: ")
        if opcao == "1":
            adicionar_sessao()
        elif opcao == "2":
            listar_sessoes()
        elif opcao == "0":
            print("SAINDO.....")
            input("PRESIONE ENTER PARA SAIR")
            break
        else:
            print("OPCAO INVALIDA!")
menu()