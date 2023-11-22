import random
import string
import csv
from shutil import copyfile

class Item:
    def __init__(self, codigo, nome, descricao, condicao, fotos=[]):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.condicao = condicao
        self.fotos = fotos

def gerar_codigo_unico(tamanho=6):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

class Cliente:
    def cadastrar_item(self, nome, descricao, condicao, fotos=[]):
        codigo = gerar_codigo_unico()
        novo_item = Item(codigo, nome, descricao, condicao, fotos)
        self.salvar_fotos(novo_item)
        return novo_item

    def salvar_fotos(self, item):
        for i, foto in enumerate(item.fotos):
            novo_nome = f"{item.codigo}_{i+1}.jpg"
            try:
                copyfile(foto, novo_nome)
                item.fotos[i] = novo_nome
            except FileNotFoundError:
                print("Erro! Foto não encontrada")

    def salvar_item_csv(self, item):
        with open('itens.csv', 'a', newline='') as csvfile:
            fieldnames = ['codigo', 'nome', 'descricao', 'condicao', 'fotos']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'codigo': item.codigo, 'nome': item.nome, 'descricao': item.descricao, 'condicao': item.condicao, 'fotos': ','.join(item.fotos)})

    def listar_itens_cadastrados(self):
        with open('itens.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"ID: {row['codigo']}, Nome: {row['nome']}")

class Funcionario:
    def avaliar_item(self, id, justificativa=None):
        try:
            pontuacao = float(input(f"Pontuação do Item {id}: "))
        except ValueError:
            print("Erro! Pontuação inválida.")
            return

        if pontuacao >= 5:
            status = "Aprovado"
        else:
            status = "Não Aprovado"
            if justificativa is None:
                justificativa = str(input("Justificativa: "))

        with open('avaliacoes.csv', 'a', newline='') as csvfile:
            fieldnames = ['id', 'status', 'justificativa']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'id': id, 'status': status, 'justificativa': justificativa})

        print("Avaliação Salva!")

    def listar_itens_cadastrados(self):
        cliente = Cliente()
        cliente.listar_itens_cadastrados()

    def ver_itens_avaliados(self):
        print("=-=" * 10)
        print("Itens Avaliados:")
        with open('avaliacoes.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"ID: {row['id']}, Status: {row['status']}")
                if 'justificativa' in row and row['justificativa']:
                    print(f"Justificativa: {row['justificativa']}")
        print("=-=" * 10)


def modulo1():
    cliente = Cliente()
    while True:
        print("=-=" * 10)
        print("[ 1 ] Cadastrar item\n[ 2 ] Sair")
        escolha = input("-> ")
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 1:
                nome = input("Nome: ")
                descricao = input("Descrição: ")
                condicao = input("Condição: ")
                escolha_fotos = input("Fotos?\n[ 1 ] Sim\n[ 2 ] Não\n-> ")
                if escolha_fotos.isdigit():
                    escolha_fotos = int(escolha_fotos)
                    if escolha_fotos == 1:
                        try:
                            foto = input("Foto: ")
                            item_cliente = cliente.cadastrar_item(nome, descricao, condicao, [foto])
                        except FileNotFoundError:
                            print("Erro! Foto não encontrada")
                    elif escolha_fotos == 2:
                        print("Nenhuma foto a ser anexada!")
                        item_cliente = cliente.cadastrar_item(nome, descricao, condicao)
                    else:
                        print("Opção Invalida!")
                    cliente.salvar_item_csv(item_cliente)
                    print("Item Cadastrado!")
                else:
                    print("Opção Inválida!")
            elif escolha == 2:
                print("Saindo. . .")
                break
            else:
                print("Opção Invalida!")
        else:
            print("Opção Inválida! Digite um número.")

def modulo2():
    funcionario = Funcionario()
    while True:
        print("=-=" * 10)
        print("[ 1 ] Avaliar item\n[ 2 ] Lista de itens cadastrados\n[ 3 ] Ver itens avaliados\n[ 4 ] Sair")
        escolha = input("-> ")
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 1:
                id_item = input("ID do item: ")
                funcionario.avaliar_item(id_item)
            elif escolha == 2:
                print("=-=" * 10)
                print("Itens e ID:")
                cliente = Cliente()
                cliente.listar_itens_cadastrados()
                print("=-=" * 10)
            elif escolha == 3:
                funcionario.ver_itens_avaliados()
            elif escolha == 4:
                print("Saindo. . .")
                break
            else:
                print("Opção Inválida!")
        else:
            print("Opção Inválida! Digite um número.")
