# menu.py
import random
import string
import csv
from shutil import copyfile
from collections import Counter
import os 
def alterar_senha(lista_senhas, cargo):
  nova_senha = input(f"Digite a nova senha para {cargo}: ")
  lista_senhas[cargo] = nova_senha
  print(f"Senha de {cargo} alterada com sucesso!")

def obter_senha(lista_senhas, cargo):
  return lista_senhas.get(cargo)

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


def modulo_1():
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
                menu_cliente()
            else:
                print("Opção Invalida!")
        else:
            print("Opção Inválida! Digite um número.")

def modulo_2():
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
                menu_funcionario()
            else:
                print("Opção Inválida!")
        else:
            print("Opção Inválida! Digite um número.")


def modulo_3():
    class SistemaGestaoCreditos:
        def __init__(self, nome_arquivo='clientes.csv'):
            self.nome_arquivo = nome_arquivo
            self.clientes = self.carregar_clientes()

        def carregar_clientes(self):
            try:
                with open(self.nome_arquivo, 'r', newline='') as arquivo:
                    leitor_csv = csv.DictReader(arquivo)
                    return {linha['nome']: {'creditos': int(linha['creditos']), 'itens_aprovados': []} for linha in leitor_csv}
            except FileNotFoundError:
                return {}

        def salvar_clientes(self):
            with open(self.nome_arquivo, 'w', newline='') as arquivo:
                campos = ['nome', 'creditos']
                escritor_csv = csv.DictWriter(arquivo, fieldnames=campos)
                escritor_csv.writeheader()
                for nome, dados in self.clientes.items():
                    escritor_csv.writerow({'nome': nome, 'creditos': dados['creditos']})

        def adicionar_cliente(self, nome_cliente):
            if nome_cliente not in self.clientes:
                self.clientes[nome_cliente] = {'creditos': 0, 'itens_aprovados': []}
                print(f'Cliente {nome_cliente} adicionado com sucesso!')
                self.salvar_clientes()
            else:
                print(f'Cliente {nome_cliente} já existe.')

        def adicionar_item_aprovado(self, nome_cliente, descricao_item, valor_credito):
            if nome_cliente in self.clientes:
                self.clientes[nome_cliente]['itens_aprovados'].append({'descricao': descricao_item, 'valor': valor_credito})
                self.clientes[nome_cliente]['creditos'] += valor_credito
                print(f'Item aprovado adicionado com sucesso para o cliente {nome_cliente}.')
                self.salvar_clientes()
            else:
                print(f'Cliente {nome_cliente} não encontrado.')

        def obter_creditos_cliente(self, nome_cliente):
            if nome_cliente in self.clientes:
                return self.clientes[nome_cliente]['creditos']
            else:
                print(f'Cliente {nome_cliente} não encontrado.')
                return None

def modulo_4():
  def ver_catalogo():
    with open('catalogo.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
  
        for linha in leitor_csv:
            print(", ".join(linha))
  
  
    menu = int(input("1- Acessar Catálogo\n"))
  
    if menu == 1:
      ver_catalogo()
  
    else:
      print("Opção inválida!")

def modulo_5():
  class SistemaTrocaItens:
      def __init__(self, nome_arquivo='clientes_troca_itens.csv'):
          self.nome_arquivo = nome_arquivo
          self.clientes = self.carregar_clientes()
  
      def carregar_clientes(self):
          try:
              with open(self.nome_arquivo, 'r', newline='') as arquivo:
                  leitor_csv = csv.DictReader(arquivo)
                  return {linha['nome']: {'creditos': int(linha['creditos']), 'itens_selecionados': []} for linha in leitor_csv}
          except FileNotFoundError:
              return {}
  
      def salvar_clientes(self):
          with open(self.nome_arquivo, 'w', newline='') as arquivo:
              campos = ['nome', 'creditos']
              escritor_csv = csv.DictWriter(arquivo, fieldnames=campos)
              escritor_csv.writeheader()
              for nome, dados in self.clientes.items():
                  escritor_csv.writerow({'nome': nome, 'creditos': dados['creditos']})
  
      def adicionar_cliente(self, nome_cliente, saldo_inicial=0):
          if nome_cliente not in self.clientes:
              self.clientes[nome_cliente] = {'creditos': saldo_inicial, 'itens_selecionados': []}
              print(f'Cliente {nome_cliente} adicionado com sucesso!')
              self.salvar_clientes()
          else:
              print(f'Cliente {nome_cliente} já existe.')
  
      def adicionar_item_selecionado(self, nome_cliente, descricao_item, valor_credito):
          if nome_cliente in self.clientes:
              if self.clientes[nome_cliente]['creditos'] >= valor_credito:
                  self.clientes[nome_cliente]['itens_selecionados'].append({'descricao': descricao_item, 'valor': valor_credito})
                  self.clientes[nome_cliente]['creditos'] -= valor_credito
                  print(f'Item selecionado adicionado com sucesso para o cliente {nome_cliente}.')
                  print(f'Saldo atual de créditos: {self.clientes[nome_cliente]["creditos"]}')
                  self.salvar_clientes()
              else:
                  print(f'Cliente {nome_cliente} não possui créditos suficientes para adquirir este item.')
          else:
              print(f'Cliente {nome_cliente} não encontrado.')
  
      def obter_itens_selecionados(self, nome_cliente):
          if nome_cliente in self.clientes:
              return self.clientes[nome_cliente]['itens_selecionados']
          else:
              print(f'Cliente {nome_cliente} não encontrado.')
              return None
def modulo_6():
  def ver_historico():
    with open('doacoes.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
  
        for linha in leitor_csv:
            print(", ".join(linha))
  
  def doar_itens():
    nome = input("Nome do produto:\n")
    ref = input("Referência do produto:\n")
    qnt = input("Quantidade de itens doados:\n")
  
    doacoes = [nome, ref, qnt]
  
    salva_doacoes(doacoes)
  
  def salva_doacoes(doacoes):
    with open("doacoes.csv", mode="a", newline="") as file:
      writer = csv.writer(file)
  
      writer.writerow(doacoes)
  
    menu = int(input("1- Realizar doação\n2- Histórico de doações\n"))
  
    if menu == 1:
      doar_itens()
  
    elif menu == 2:
      ver_historico()
  
def modulo_7():
  def lerArquivo(nomeArquivo):
      with open(nomeArquivo, 'r') as arquivo:
          linhas = arquivo.readlines()
      return linhas

  def gerar_relatorio(linhas):
      total_cadastrados = len(linhas)
      total_avaliados = 0
      total_trocados = 0
      total_doados = 0

      for linha in linhas:
          dados = linha.split(',')
          # Supondo estrutura do arquivo: nome, status (Cadastrado/Avaliado/Trocado/Doado)
          if "Avaliado" in dados[1]:
              total_avaliados += 1
          elif "Trocado" in dados[1]:
              total_trocados += 1
          elif "Doado" in dados[1]:
              total_doados += 1

      return total_cadastrados, total_avaliados, total_trocados, total_doados

  def gerar_relatorio_csv(nome_arquivo_de_saida, relatorio):
      with open(nome_arquivo_de_saida, 'w', newline='') as arquivo_csv:
          escritor_csv = csv.writer(arquivo_csv)
          escritor_csv.writerow(['total cadastrados', 'total avaliados', 'total trocados', 'total doados'])
          escritor_csv.writerow(relatorio)

  def gerar_relatorio_txt(nome_arquivo_saida, relatorio):
      with open(nome_arquivo_saida, 'w') as arquivo_txt:
          arquivo_txt.write("relatorio\n")
          arquivo_txt.write(f"rotal cadastrados: {relatorio[0]}\n")
          arquivo_txt.write(f"total avaliados: {relatorio[1]}\n")
          arquivo_txt.write(f"total trocados: {relatorio[2]}\n")
          arquivo_txt.write(f"total doados: {relatorio[3]}\n")

  def main():
      nome_arquivo_entrada = input("digite o nome do arquivo de entrada: ")
      escolha_saida = input("escolha o formato de saida (csv/txt): ").lower()
      nome_arquivo_saida = input("digite o nome do arquivo de saida: ")

      linhas = ler_arquivo(nome_arquivo_entrada)
      relatorio = gerar_relatorio(linhas)

      if formato_saida == 'csv':
          gerar_relatorio_csv(nome_arquivo_saida, relatorio)
      elif formato_saida == 'txt':
          gerar_relatorio_txt(nome_arquivo_saida, relatorio)
      else:
          print("formato de saida invalido. escolha 'csv' ou 'txt'.")

  if __name__ == "__main__":
      main()

def salvar_produtos(filename, produtos):
  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(produtos[0].keys())
    for produto in produtos:
        writer.writerow(produto.values())

def cadastrar_produtos(produtos):
  nome = input('Digite o nome do produto: ')
  categoria = input('Digite a categoria do produto: ')
  preco = float(input('Digite o preço unitário do produto: '))
  quantidade = int(input('Digite a quantidade em estoque do produto: '))

  produtos_dic = {
    'Nome': nome,
    'Categoria': categoria,
    'Preço unitário': preco,
    'Quantidade em estoque': quantidade
  }

  produtos.append(produtos_dic)
  salvar_produtos('Lista_produtos_venda.csv', produtos)

def venda_produtos(produtos):
  nome_produto = input('Digite o nome do produto vendido: ')
  quantidade_vendida = int(input('Digite a quantidade vendida deste produto: '))
  data_venda = input('Digite a data da venda (dd/mm/aaaa): ')

  encontrado = False

  for produto in produtos:
      if produto['Nome'].lower() == nome_produto.lower():
          encontrado = True
          if produto['Quantidade em estoque'] >= quantidade_vendida:
              produto['Quantidade em estoque'] -= quantidade_vendida
              # Adiciona a data da venda ao dicionário do produto
              if 'Vendas' not in produto:
                  produto['Vendas'] = []
              produto['Vendas'].append({
                  'Quantidade': quantidade_vendida,
                  'Data': data_venda
              })
              print(f'{quantidade_vendida} unidades de {nome_produto} vendidas com sucesso!')
              salvar_produtos('Lista_produtos_venda.csv', produtos)
          else:
              print('Quantidade em estoque insuficiente para realizar a venda.')

  if not encontrado:
      print('Produto não encontrado.')

produtos = []

def balanco_vendas(produtos):
  data_inicio = input('Digite a data de início do período (dd/mm/aaaa) ou deixe em branco para não filtrar por data: ')

  print('\n')

  data_fim = input('Digite a data de fim do período (dd/mm/aaaa) ou deixe em branco para não filtrar por data: ')

  print('\n')

  categoria_filtro = input('Digite a categoria para filtrar as vendas (deixe em branco para mostrar todas as categorias): ')

  vendas_totais = 0  # Variável para armazenar o valor total das vendas

  for produto in produtos:
      if 'Vendas' in produto:
          vendas_produto = produto['Vendas']
          total_vendas_produto = 0

          for venda in vendas_produto:
              venda_data = datetime.strptime(venda['Data'], '%d/%m/%Y')

              # Verifica se a venda está dentro do intervalo de datas especificado
              if (not data_inicio or datetime.strptime(data_inicio, '%d/%m/%Y') <= venda_data) and \
                (not data_fim or datetime.strptime(data_fim, '%d/%m/%Y') >= venda_data):
                  if not categoria_filtro or produto['Categoria'].lower() == categoria_filtro.lower():
                      total_vendas_produto += venda['Quantidade']

          if total_vendas_produto > 0:
              print(f"No período de {data_inicio or 'todo o tempo'} a {data_fim or 'hoje'}, foram vendidas {total_vendas_produto} unidades do produto {produto['Nome']} \n.")
              vendas_totais += total_vendas_produto

  print(f"Valor total das vendas: {vendas_totais}")

#Menu principal
def manu():
  while True:
    print('=-' * 20)
    print("\nMenu Principal:")
    print("1. Cadastrar Produto")
    print("2. Venda de Produtos")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")
    print('\n')

    if escolha == '1':
        cadastrar_produtos(produtos)
    elif escolha == '2':
        venda_produtos(produtos)
    elif escolha == '3':
        menu_funcionario()
    else:
        print("Opção inválida. Escolha uma opção válida.")

def manu_2():
  while True:
    print('=-' * 20)
    print("\nMenu Principal:")
    print("1. Balanço de vendas")
    
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
      balanco_vendas(produtos)
    elif escolha == '2':
      menu_gerente()
    else:
      print("Opção inválida. Escolha uma opção válida.")

def modulo_10():
  def ler_arquivo_vendas(nome_arquivo):
      with open(nome_arquivo, 'r') as arquivo:
          linhas = arquivo.readlines()
      return linhas

  def ler_arquivo_trocas(nome_arquivo):
      with open(nome_arquivo, 'r') as arquivo:
          linhas = arquivo.readlines()
      return linhas

  def gerar_relatorio_vendas(linhas):
      total_vendas = 0

      for linha in linhas:
          dados = linha.split(',')
          # Supondo estrutura do arquivo: nome, quantidade, valor
          total_vendas += int(dados[1])

      return total_vendas

  def gerar_relatorio_trocas(linhas):
      total_trocas = len(linhas)
      produtos_populares = []

      for linha in linhas:
          dados = linha.split(',')
          # Supondo a estrutura do arquivo: nome_produto, motivo_troca
          produtos_populares.append(dados[0])


      produtos_mais_populares = Counter(produtos_populares).most_common(3)

      return total_trocas, produtos_mais_populares

  def gerar_relatorio_gerente(nome_arquivo_vendas, nome_arquivo_trocas):
      linhas_vendas = ler_arquivo_vendas(nome_arquivo_vendas)
      linhas_trocas = ler_arquivo_trocas(nome_arquivo_trocas)

      total_vendas = gerar_relatorio_vendas(linhas_vendas)
      total_trocas, produtos_mais_populares = gerar_relatorio_trocas(linhas_trocas)

      return total_vendas, total_trocas, produtos_mais_populares

  def gerar_relatorio_gerente_csv(nome_arquivo_saida, relatorio):
      with open(nome_arquivo_saida, 'w', newline='') as arquivo_csv:
          escritor_csv = csv.writer(arquivo_csv)
          escritor_csv.writerow(['total vendas', 'total trocas', 'produtos mais populares'])
          escritor_csv.writerow(relatorio)

  def main():
      nome_arquivo_vendas = input("digite o nome do arquivo de vendas: ")
      nome_arquivo_trocas = input("digite o nome do arquivo de trocas: ")
      nome_arquivo_saida = input("digite o nome do arquivo de saida: ")

      relatorio_gerente = gerar_relatorio_gerente(nome_arquivo_vendas, nome_arquivo_trocas)

      gerar_relatorio_gerente_csv(nome_arquivo_saida, relatorio_gerente)

  if __name__ == "__main__":
      main()
    
def login(cargos, lista_senhas):
    cargo = input("Digite seu cargo (gerente/funcionario/cliente): ").lower()

    if cargo == 'cliente':
        return True, 'cliente'
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

def ver_catalogo():
  with open('catalogo.csv', 'r', newline='') as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)

      for linha in leitor_csv:
          print(", ".join(linha))


  menu = int(input("1- Acessar Catálogo\n"))

  if menu == 1:
    ver_catalogo()

  else:
    print("Opção inválida!")


def menu_gerente(senhas):
    print("Bem-vindo, gerente!")
    print("1- Relatorios e Estatisticas \n 2- Balanco de Vendas \n 3- Relatorios Estatisticos \n 4- Sair \n")

    chave = input('')

    while True:
        if chave == '1':
            modulo_7()
        elif chave == '2':
            manu_2()
        elif chave == '3':
            modulo_10()
        elif chave == '4':
            print('Saindo...')
            exit()
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
            modulo_2()
        elif chave == '2':
            modulo_3()
        elif chave == '3':
            manu()# Modificar para a função correta
        elif chave == '4':
            break
        else:
            print('ERROR 404 (nao existe)')

def menu_cliente():
    print("Bem-vindo, cliente!")
    print("1- Cadastro de Itens \n 2- Catalogo de Itens Disponiveis \n 3- Trocas de Itens \n 4- Doacao de Itens \n 5- Sair\n")

    while True:
      chave = input('')
      if chave == '1':
          modulo_1()
      elif chave == '2':
          modulo_4()
      elif chave == '3':
          modulo_5()
      elif chave == '4':
          modulo_6()
      elif chave == '5':
          print('Saindo...')
          exit()
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
