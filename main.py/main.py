import os
import sqlite3

conexao = sqlite3.connect('sessoes.db')


sessoes = []

def limpar_dados():
    os.system("cls" if os.name == "nt" else "clear")

def adicionar_sessao():
    #id: gerar id 
    nome = input("Digite Seu nome: ")
    assunto = input("Qual assunto que gostaria de registrar: ")
    while True:
        try:
            dificuldade = int(input("Qual a dificuldade do assunto adicionado: [1 - 10]: "))
        except ValueError:
            print ("colocar apenas numero!")
            continue
        if dificuldade > 0 and dificuldade <=10:
            break
        else:
            print("COLOCAR DE 1 A 10")

    horas = 0
    salvar = {
        "nome":nome.strip(),
        "assunto":assunto.strip(),
        "dificuldade":dificuldade,
        "horas":horas
    }
    print('Sessão cadastrada com sucesso!')
    input('Aperte enter para continuar')
    sessoes.append(salvar)
    limpar_dados()
#adicionar_sessao()

def listar_sessoes():
    if len(sessoes) == 0:
        print("NENHUMA SESSAO CADASTRADA!")
        return
    
    for sessao in sessoes:
        print(f"Nome: {sessao['nome']}")
        print(f"Assunto: {sessao['assunto']}")
        print(f"Dificuldade: {sessao['dificuldade']}")
        print(f"Horas estudadas: {sessao['horas']}")
#listar_sessoes()

def remover_sessao():
    if len(sessoes) == 0:
        print("NENHUMA SESSAO CADASTRADA!")
        return  
    
    buscar = input('Informe o assunto a ser removido: ')
    for sessao in sessoes:
        if buscar == sessao['assunto']:
            print('foi removido')
            sessoes.remove(sessao)
        else:
            print('Nenhuma sessão foi encontrada')
    limpar_dados()

#remover_sessao()
#listar_sessoes()

def atualizar_sessao():
    if len(sessoes) == 0:
        print("NENHUMA SESSAO CADASTRADA!")
        return   
    buscar = input('Digite o assunto que deseja atualizar: ')
    for sessao in sessoes:
        if buscar == sessao['assunto']:
            novo_assunto = input('Digite o novo assunto: ')
            sessao['assunto'] = novo_assunto
            while True:
                try:
                     nova_dificuldade = int(input("Qual a dificuldade do assunto adionado: [1 - 10]"))
                except ValueError:
                    print ("colocar apenas numero!")
                    continue
                if nova_dificuldade > 0 and nova_dificuldade <=10:
                    break
                else:
                    print("COLOCAR DE 1 A 10")
            sessao['dificuldade'] = nova_dificuldade
            while True:
                try:
                    nova_hora = int(input("Digite a quantidade de horas estudadas: "))
                    break
                except ValueError:
                    print ("colocar apenas numero!")
                    continue
            sessao['hora'] = nova_hora
        else:
            print('não encontrou')
    limpar_dados()
    
#listar_sessoes()
#
# atualizar_sessao()
#limpar_dados()
while True:
    #limpar_dados()
    print('1 - Adicionar sessão')
    print('2 - Listar sessões')
    print('3 - Remover sessão')
    print('4 - Atualizar sessão')
    print('0 - Sair')
    opcao = input('Digite a opção: ')
    if opcao == '0':
        print('Programa finalizado!')
        break
    elif opcao == '1':
        adicionar_sessao()
    elif opcao == '2':
        listar_sessoes()
    elif opcao == '3':
        remover_sessao()
    elif opcao == '4':
        atualizar_sessao()
    else:
        print('opcão invalida')
        input('pressione enter para voltar')