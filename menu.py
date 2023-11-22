# menu.py
from senha import alterar_senha, obter_senha

def login(cargos, lista_senhas):
    cargo = input("Digite seu cargo (gerente/funcionario/cliente): ").lower()

    if cargo == 'cliente':
        return True  # Acesso direto para clientes sem senha
    elif cargo in cargos:
        senha_digitada = input("Digite a senha: ")
        senha_armazenada = obter_senha(lista_senhas, cargo)

        if senha_digitada == senha_armazenada:
            return True, cargo
        else:
            print("Senha incorreta. Tente novamente.")
            return False, None
    else:
        print("Cargo não reconhecido. Tente novamente.")
        return False, None

def menu_gerente(senhas):
    print("Bem-vindo, gerente!")
    print("1- Relatorios e Estatisticas \n 2- Balanco de Vendas \n 3- Relatorios Estatisticos \n 4- Sair \n")
    chave = input('')
    while True:
    if chave == '1':
      modulo()
    elif chave == '2':
      modulo()
    elif chave == '3':
      modulo()
    elif chave == '4':
      break
    else:
      print('ERROR 404 (nao existe)')

        opcao = input("Digite o número da opção (ou 's' para sair): ")

        if opcao == '1':
            alterar_senha(senhas, 'gerente')
        elif opcao == '2':
            print("Acesso ao Módulo 1 - Gerente")
        elif opcao == '3':
            print("Acesso ao Módulo 2 - Gerente")
        elif opcao == '4':
            print("Acesso Cliente - Gerente")
        elif opcao.lower() == 's':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionario():
    print("Bem-vindo, funcionário!")
    print("1- Avaliacao de itens \n 2- Gestao de creditos \n 3-Gestao de Estoque de Produtos a Venda \n 4- Sair \n")
    chave = input('')
    while True:
    if chave == '1':
      modulo()
    elif chave == '2':
      modulo()
    elif chave == '3':
      modulo()
    elif chave == '4':
      break
    else:
      print('ERROR 404 (nao existe)')

def menu_cliente():
    print("Bem-vindo, cliente!")
    print("1- Cadastro de Itens \n 2- Catalogo de Itens Disponiveis \n 3- Trocas de Itens \n 4- Doacao de Itens \n 5- Sair\n")
    chave = input('')
    while True:
    if chave == '1':
      modulo()
    elif chave == '2':
      modulo()
    elif chave == '3':
      modulo()
    elif chave == '4':
      modulo()
    elif chave == '5':
      break
    else:
      print('ERROR 404 (nao existe)')

def main():
    cargos = ['gerente', 'funcionario', 'cliente']
    senhas = {'gerente': 'senha_gerente', 'funcionario': 'senha_funcionario', 'cliente': ''}

    while True:
        sucesso, cargo = login(cargos, senhas)
        if sucesso:
            break

    if cargo == 'gerente':
        menu_gerente(senhas)
    elif cargo == 'funcionario':
        menu_funcionario()
    elif cargo == 'cliente':
        menu_cliente()

if __name__ == "__main__":
    main()
