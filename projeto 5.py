#🐍 PROJETO 5 — “Controle de Metas de Estudo”
#Subtítulo: planejar, acompanhar e ajustar seu progresso
import os
def limpar_dados():
    os.system("cls" if os.name == 'nt' else "clear")
listas = []
def criar_meta():
    nome_meta = input("Qual e o nome da sua meta: ")
    while True:
        try:
            horas_planejadas = float(input("Quais sao as horas planejadas dessa meta: "))
            break
        except ValueError:
            print("OPS..... NAO E POSSIVEL DIGITAR LETRAS, DIGITAR APENAS NUMERO!")
            continue
    horas_realizadas = 0
    status = "EM ANDAMENTO"
    print("LISTA CRIADA COM SUCESSO!")
    input("Pressione enter para voltar ao menu")
    limpar_dados()
    salvar = {
        "nome":nome_meta,
        "horas_planejadas":horas_planejadas,
        "horas_realizadas":horas_realizadas,
        "status":status
    }
    listas.append(salvar)


def lista_metas():
    if len(listas) == 0:
        print("SEM LISTA NO MOMENTO")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
        limpar_dados()
        return
    for lista in listas:
        print("======Estas sao suas lista de metas ========")
        print(f"sua meta {lista['nome']}, suas horas planejadas sao {lista['horas_planejadas']} horas ")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
        limpar_dados()
def registrar_horas():
    meta = input("Qual meta voce gostaria de atualizar : ")
    for lista in listas:
        if meta == lista['nome']:
            print("Meta encontrada com sucesso")
            while True:
                try:
                    new_horas = float(input("Quantas horas voce realizou: "))
                    break
                except ValueError:
                    print("OPS DEU ALGUM ERRO POR GENTILEZA, COLOCAR APENAS NUMERO!")
            if new_horas < lista['horas_planejadas']:
                lista['status'] = "EM ANDAMENTO"
            elif new_horas == lista['horas_planejadas']:
                lista['status'] = "Concluido"
            elif new_horas > lista['horas_planejadas']:
                lista['status'] = "UTRAPASSADO"  
            lista["horas_realizadas"] += new_horas
            print("Horas adicionada com sucesso")
            input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
            limpar_dados()
            break
    else:
        print("meta nao econtrada!!")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
        limpar_dados()
def avaliar_meta():
    meta = input("Qual meta voce gostaria de avaliar: ")
    for lista in listas:
        if meta == lista["nome"]:
            print("lista selecionada com sucesso")
            if lista["horas_realizadas"] < lista["horas_planejadas"]:
                print(f"Essa meta ainda nao foi concluida, voce fez {lista['horas_realizadas']}, e a horas planejada e de {lista['horas_planejadas']}")
                lista['status'] = "EM ANDAMETO"
                input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
                limpar_dados()
                break
            elif lista['horas_planejadas'] == lista['horas_realizadas']:
                print("Meta Concluida")
                lista['status'] = "Concluida"
                input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
                limpar_dados()
                break
            elif lista['horas_realizadas'] > lista["horas_planejadas"]:
                print("Voce utrapassou a meta planejada parabens")
                lista['status'] = "META UTRAPASSADA"
                input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
                limpar_dados()
                break
    else:
        print("Meta nao econtrada!")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
        limpar_dados()
def menu():
    while True:
        print("===============BEM VINDOS AO CONTROLE DE METAS MENU ===============")
        print("1 - Criar metas")
        print("2 - listar metas")
        print("3 - registrar horas")
        print("4 - avaliar metas")
        print("5 - Sair do menu")
        opcao = input("DIGITE UMA OPCAO: ")
        if opcao == "1":
            criar_meta()
        elif opcao == "2":
            lista_metas()
        elif opcao == "3":
            registrar_horas()
        elif opcao == "4":
            avaliar_meta()
        elif opcao == "5":
            print("Saindo do sistema.....")
            input("PRESSIONE ENTER PARA SAIR....")
            limpar_dados()
            break
menu()



    

            

