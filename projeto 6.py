#🐍 PROJETO 6 — “Diário de Sessões de Estudo”
#Objetivo: registrar cada sessão de estudo, não só metas ou semanas.
import os
import json
def salvar_em_arquivo():
    with open("arquivos.json", "w") as aqruiv_json:
        return json.dump(arquivos, aqruiv_json )
def carregar_arquivo():
    try:
        with open("arquivos.json", "r") as arquivv_json:
            arquivos = json.load(arquivv_json)
    except FileNotFoundError:
        arquivos = []
def limpar_dados():
    os.system("cls" if os.name == "nt" else "clear")
arquivos = []
def sessao():
    assunto = input("Dgite o assunto da sessao de estudio: ")
    while True:
        try:
            horas = float(input("Digite a duracao de horas da sessao: "))
            break
        except ValueError:
            print("ops...colocar apenas numeros! sem letras")
            continue
    dia =  input("INFORME A DATA DA SESSAO: (EX:2026-01-25)")
    obs = input("Digite uma observacao da sessao: ")
    salvar = {
        "assunto":assunto,
        "horas":horas,
        "dia":dia,
        "obs":obs,
    }
    arquivos.append(salvar)
    salvar_em_arquivo()

def historico():
    if len(arquivos) == 0:
        print("Sem nehum registro de sessao")
        return
    total_horas = 0
    for sessao in arquivos:
        print(f"sessao registrada com assunto: {sessao['assunto']},"
        f"{sessao['horas']} horas, dia {sessao['dia']},"
        f"observacao {sessao['obs']}, e dia {sessao['dia']}")
        total_horas += sessao['horas']
    print("======================")
    print(f"Total de horas estudadas, {total_horas}h")

def analise():
    if len(arquivos) == 0:
        print("Nenhuma sessao registrada!")
        return
    somar = 0
    for arquivo in arquivos:
        somar += arquivo['horas']
    media = somar / len(arquivos)
    print(f"TOTAL DE SESSOES: {len(arquivos)},"
    f"TOTAL DE HORAS ESTUDADAS: {somar},"
    f"MEDIA DE HORAS ESTUDADAS: {media}")


def mini_menu():
    carregar_arquivo()
    while True:
        print("Mini menu")
        print("1 - registrar sessao")
        print("2 - mostrar historico")
        print("3 - Analisar sessao")
        print("0 - sair")
        opcao = input("digite uma opcao: ")
        if opcao == "1":
            limpar_dados()
            sessao()
        elif opcao == "2":
            limpar_dados()
            historico()
        elif opcao == "3":
            analise()
        elif opcao == "0":
            limpar_dados()
            print("saindo....")
            break
        else:
            print("opcao invalida!")
mini_menu()
                
        

    

