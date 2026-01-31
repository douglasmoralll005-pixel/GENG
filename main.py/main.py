import os
sessoes = []
def limpar_dados():
    os.system("cls" if os.name == "nt" else "clear")
def adicionar_sessao():
    #id: gerar id 
    nome = input("Digite Seu nome: ")
    assunto = input("Qual assunto que gostaria de registrar: ")
    while True:
        try:
            dificuldade = int(input("Qual a dificuldade do assunto adionado: [0 - 10]"))
        except ValueError:
            print ("colocar apenas numero!")
            continue
        if dificuldade >0 and dificuldade <10:
            break
        else:
            print("COLOCAR DE 0 A 10")

    horas = 0
    salvar = {
        "nome":nome.strip(),
        "assunto":assunto.strip(),
        "dificuldade":dificuldade,
        "horas":horas
    }
    sessoes.append(salvar)
adicionar_sessao()

def listar_sessoes():
    if len(sessoes) == 0:
        print("NEHUMA SESSAO CADASTRADA!")
        return
    
    for sessao in sessoes:
        print(f"Nome: {sessao['nome']}")
        print(f"Assunto: {sessao['assunto']}")
        print(f"dificuldade: {sessao['dificuldade']}")
        print(f"Horas estudadas: {sessao['horas']}")
listar_sessoes()

