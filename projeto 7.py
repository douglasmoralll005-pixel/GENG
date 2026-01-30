import json
jogos = []
def salvar_em_arquivo():
    with open("jogos.json", "w" ) as arquivos:
        json.dump("jogos.json", arquivos)
def carregar_arquivo():
    try:
        with open("jogos.json", "r") as arquivos:
            jogos = json.load(arquivos)
    except FileNotFoundError:
        jogos = []
def adicionar_jogo():
    nome = input("DIGITE NOME DO GAME QUE DESEJA ADICIONAR A LISTA: ")
    genero = input("DIGITE O GENERO DO JOGO: ")
    plataforma = input("QUAL PLATAFORMA QUE O JOGO RODA: ")
    while True:
        try:
            nota = float(input("Que nota voce da para o game: "))
            break
        except ValueError:
            print("ERROR COLOCAR APENAS NUMERO!")
            continue
    salvar = {
        "nome":nome,
        "genero":genero,
        "plataforma":plataforma,
        "nota":nota
    }
    jogos.append(salvar)
    salvar_em_arquivo
def lista_game():
    if len(jogos) == 0:
        print("SEM REGISTRO DE JOGOS")
        return
    for jogo in jogos:
        print("==========LISTA DE JOGOS =====")
        print(f"Nome:{jogo['nome']},")
        print(f"genero:{jogo['genero']},")
        print(f"Plataforma:{jogo['plataforma']},")
        print(f"Nota:{jogo['nota']}")
def menu():
    carregar_arquivo()
    while True:
        print("======== BEM VINDO AO MENU =========")
        print("1 - Adicionar jogo")
        print("2 - Listar jogos")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            adicionar_jogo()
        elif opcao == "2":
            lista_game()
        elif opcao == "0":
            print("Saindo.....")
            input("PRESIONE ENTER PARA SAIR....")
            break
        else:
            print("OPCAO INVALIDA!")
menu()