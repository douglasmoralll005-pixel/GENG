#🐍 PROJETO 3 — “Diário de Evolução”
#Subtítulo: Um programa que lembra do seu progresso
horas = []
nome = input("Qual seu nome: ").strip()
def horas_estudo():
    while True:
        try:
            horario = int(input("Quantas horas estudou na semena: "))
            break
        except ValueError:
            print("Digitar apenas numero! Sem letras!")
            continue
    horas.append(horario) 
def somar_horas():
    if len(horas) == 0:
        print("nehuma hora adicionada ainda.")
        return
    print("Vamos fazer a soma das suas horas")
    somar = 0
    for hora in horas:
        somar += hora
    print(f"Voce tem o total de {somar}, somadas!")
def media_horas():
    print("Vamos tirar a media de horas")
    media = 1
    soma = 0
    if len(horas) == 0:
        print("nehuma hora adicionada")
        return
    for hora in horas:
        soma += hora
    resultado = soma / len(horas)
    print(f"A media de horas acumulada [e de {resultado}]")
def menu():
    while True:
        print("1 - Registrar semana")
        print("2 - Mostrar todas as horas registradas")
        print("3- Somar horas da semana")
        print("4 - tirar a media de horas")
        print("0- sair")
        opcoes = input("Digite uma opcao:")
        if opcoes == "1":
            horas_estudo()
        elif opcoes == "2":
            print("Aqui estao suas horas de estudos")
            for hora in horas:
                print(hora)
        elif opcoes == "3":
            somar_horas()
        elif opcoes == "4":
            media_horas()
        elif opcoes == "0":
            print("Saindo......")
            break
        else:
            print("opcao invalida!!")
menu()

