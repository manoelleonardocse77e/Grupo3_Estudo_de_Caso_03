import csv
from datetime import datetime
# Modulo 8
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
# Modulo 9
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

while True:
  print('=-' * 20)
  print("\nMenu Principal:")
  print("1. Cadastrar Produto")
  print("2. Venda de Produtos")
  print("3. Balanço de Vendas")
  print("4. Sair")

  escolha = input("Escolha uma opção: ")
  print('\n')
  
  if escolha == '1':
      cadastrar_produtos(produtos)
  elif escolha == '2':
      venda_produtos(produtos)
  elif escolha == '3':
      balanco_vendas(produtos)
  elif escolha == '4':
      break
  else:
      print("Opção inválida. Escolha uma opção válida.")