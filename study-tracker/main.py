from utils.limpa_tela import limpa_tela
from data.db import *

def cadastra_dados(nome, assunto, dificuldade, horas):
    cria_tabela()
    comando.execute("""
        INSERT INTO usuarios (nome, assunto, dificuldade, horas)
        VALUES (?, ?, ?, ?)""", (nome,assunto,dificuldade, horas))
    conexao.commit()

def remover_dados(assunto):
    comando.execute(
        "SELECT * FROM usuarios WHERE assunto = ?",
        (assunto,)
    )

    dados = comando.fetchall()
    print(dados)
    comando.execute(
        "DELETE FROM usuarios WHERE assunto = ?", (assunto,)
    )
    conexao.commit()

sessoes = []

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
    print('Sessão cadastrada com sucesso!')
    input('Aperte enter para continuar')
    limpa_tela()
    cadastra_dados(nome.strip(), assunto.strip(), dificuldade, horas)

def listar_sessoes():
    comando.execute("SELECT * FROM usuarios")
    registros = comando.fetchall()
    if len(registros) == 0:
        print("SEM SESSAO CADASTRADA!")
        return
    for r in registros:
        print(f"ID: {r[0]} | Nome: {r[1]} | Assunto: {r[2]} | Dificuldade: {r[3]} | Horas: {r[4]}")

def remover_sessao():
    comando.execute("SELECT * FROM usuarios")
    registros = comando.fetchall()
    if len(registros) == 0:
        print("SEM REGISTRO CADASTRADO!")
        return
    for r in registros:
        print(f"ID: {r[0]} | Nome: {r[1]} | Assunto: {r[2]} | Dificuldade: {r[3]} | Horas: {r[4]}")
    buscar = input('Informe o assunto a ser removido: ')
    remover_dados(buscar)
    limpa_tela()

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
    limpa_tela()
    
while True:
    print('1 - Adicionar sessão')
    print('2 - Listar sessões')
    print('3 - Remover sessão')
    print('4 - Atualizar sessão')
    print('0 - Sair')
    opcao = input('Digite a opção: ')
    if opcao == '0':
        print('Programa finalizado!')
        conexao.close() #Fecha conexão com Banco de Dados
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
        print('Opcão inválida')
        input('Pressione enter para voltar')