#Projeto 1 — “Bússola de Estudo
#Subtítulo: Um programa que te ajuda a entender seu ritmo de aprendizado
def horas_estudo():
    nome = input("Qual seu nome: ")
    horas = int(input("Quantas horas voce estuda por semana: "))
    if horas <5:
        print(f"ola, {nome} seu ritmo e lento, tudo bem se e o tempo que voce tem, e oque importa!!")
    elif horas <10:
        print(f"Ola, {nome} seu ritmo mediano, esta indo bem!")
    else:
        print(f"Ola,{nome} seu ritmo e intenso, isso e otimo!")
horas_estudo()

#BOM DEMAIS