#criar sistema bancario completo
#inicialmente só possui 1 conta
#é possivel ver saldo, sacar e depositar
#futuramente salvar contas e escolher qual acessar
#e transferir saldo entre elas

def menu_opcoes():
    print('1 - Acessar conta')
    print('0 - Sair')

while True:
    menu_opcoes()
    opcao = int(input('Informe a opção que deseja: '))
    if opcao == 0:
        print('Programa finalizado')
        break
    elif opcao == 1:
        print('Bem-vindo(a)!')
        print('Sistema em construção\nVolte mais tarde!')
        break