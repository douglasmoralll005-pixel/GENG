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
def atualizar_assunto(
    novo_assunto,
    novo_assunto1,
    nova_dificuldade,
    novas_horas
):
    comando.execute(
        """
        UPDATE usuarios
        SET assunto = ?, dificuldade = ?, horas = ?
        WHERE assunto = ?
        """,
        (novo_assunto1, nova_dificuldade, novas_horas, novo_assunto)
    )
    conexao.commit()
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
    comando.execute("SELECT * FROM usuarios")
    registros = comando.fetchall()

    if len(registros) == 0:
        print("SEM REGISTRO CADASTRADO!")
        return
    listar_sessoes()
    assunto_antigo = input("Digite o assunto que deseja atualizar: ")

    for registro in registros:
        if assunto_antigo == registro[2]:

            novo_assunto = input("Digite o novo assunto: ")

            # dificuldade
            while True:
                try:
                    nova_dificuldade = int(input("Qual a dificuldade do assunto [1 - 10]: "))
                    if 1 <= nova_dificuldade <= 10:
                        break
                    else:
                        print("COLOCAR DE 1 A 10")
                except ValueError:
                    print("Colocar apenas número!")

            # horas
            while True:
                try:
                    nova_hora = int(input("Digite a quantidade de horas estudadas: "))
                    break
                except ValueError:
                    print("Colocar apenas número!")

            # UPDATE NO BANCO
            comando.execute(
                """
                UPDATE usuarios
                SET assunto = ?, dificuldade = ?, horas = ?
                WHERE assunto = ?
                """,
                (novo_assunto, nova_dificuldade, nova_hora, assunto_antigo)
            )
            conexao.commit()

            print("Sessão atualizada com sucesso!")
            return

    print("Assunto não encontrado!")
        

    
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