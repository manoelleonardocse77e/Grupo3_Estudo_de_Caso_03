# senha.py

def alterar_senha(lista_senhas, cargo):
    nova_senha = input(f"Digite a nova senha para {cargo}: ")
    lista_senhas[cargo] = nova_senha
    print(f"Senha de {cargo} alterada com sucesso!")

def obter_senha(lista_senhas, cargo):
    return lista_senhas.get(cargo)
