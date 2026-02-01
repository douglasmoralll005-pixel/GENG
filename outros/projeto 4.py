#🐍 PROJETO 4 — “Radar de Hábitos”
#Subtítulo: Um programa que identifica padrões no seu estudo
semanas = []
def registrar_semana():
    while True:
        try:
            semana = int(input("Quantas semana voce estudou:"))
            horas = int(input("Quantas horas voce estudou: "))
            break
        except ValueError:
            print("Digite apenas numero!! Sem letras!")
            continue
    comentario = input("Digite um comentario para essas horas da semana: ")
    lista = {
        "semanas":semana,
        "Horas estudadas":horas,
        "comentario":comentario
    }
    semanas.append(lista)
def mostrar_historico():
    if len(semanas) == 0:
        print("Nenhuma semana registrada")
        return
    for semana in semanas:
        print(f"Semanas registradas{semana["semanas"]} semanas")
        print(f"Suas horas estudadas foram {semana["Horas estudadas"]} horas")
        print(f"Seus comentarios para cada hora '{semana["comentario"]}' comentarios")
        print("========================================================")
def calcular_media():
    if len(semanas) == 0:
        print("Nehuma semana registrada. Impossivel fazer a media")
        return
    somar = 0
    for semana in semanas:
        somar += semana["Horas estudadas"]
    media = somar / len(semanas)
    print(f"Essa e a media de semanas estudadas, {media}")
    return media
def analisar_padrao():
    media  = calcular_media()
    if media is None:
        return
    print(f"media de horas estudadas: {media}")
    print("Vamos analizar o padrao")
    for semana in semanas:
        if semana["Horas estudadas"] < media:
            print(f"Voce esta abaixo da media em semanas estudadas, suas horas foram {semana["semanas"]}, e {semana ["Horas estudadas"]} horas estudadas")
        elif semana["Horas estudadas"] == media:
            print(f"Voce esta na media de semanas estudadas, suas horas da semana foram {semana}")
        elif semana["Horas estudadas"] >= media:
            print(f"Voce esta acima da media de semanas estudadas, suas hora foram {semana}")
        else:
            print("Sem horas estudadas")
def menu():
    while True:
        print("1 - Registrar semana")
        print("2 - Mostrar historico")
        print("3 - calcular media")
        print("4 - analisar padrao")
        print("5 - sair ")
        opcao = input("Escolha uma opcao:")
        if opcao == "1":
            registrar_semana()
        elif opcao == "2":
            mostrar_historico()
        elif opcao == "3":
            calcular_media()
        elif opcao == "4":
            analisar_padrao()
        elif opcao == "5":
            print("Saindo do sistema....")
            input("Presione enter para sair!")
            break
        else:
            print("Opcao invalida tente novamente!")
menu()
    