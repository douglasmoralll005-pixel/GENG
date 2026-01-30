#🐍 Projeto 2 — “Treinador de Constância”
#Subtítulo: Um programa que não desiste do usuário
nome = input("Digite seu nome: ").lower().strip()
def menu(nome):
    print("BEM VINDOS AO TREINADOR DE CONSTANCIA")
    while True:
        try:
            horas = int(input("Quantas horas voce estudou essa semana: "))
        except ValueError:
            print("Digitar apenas numero!! sem letras")
            continue
        if horas <5:
            print(f"{nome}, parabens voce estudo mais que a maioria, e isso ja euma otima coisa,{horas} horas de estudo nao e facil. Otimo empenho!") #essa e a mensagem motivacional
        else:
            print(f"UAU {nome}, isso e incrivel, mostra que voce esta comprometido a aprender, {horas} horas nao sao facieis. Otimo aprendizado!") # mensagem motivacional
        pergunta = input("Quer registrar outra semana? (s/n): ").lower().strip()
        if pergunta == "s":
            print ("AGUARDE UM INSTANTE")
            continue
        else:
            print("Otima semana fique bem!")
            break
menu(nome)