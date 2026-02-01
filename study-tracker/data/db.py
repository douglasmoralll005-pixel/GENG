import sqlite3

conexao = sqlite3.connect('sessoes.db') #Conexão com Banco de Dados
comando = conexao.cursor() #Variavel responsavel por executar os comandos SQL

def cria_tabela():
    comando.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        assunto TEXT NOT NULL,
        dificuldade INTEGER,
        horas INTEGER)
        """
    )
    conexao.commit() #Serve para salvar alterações no banco