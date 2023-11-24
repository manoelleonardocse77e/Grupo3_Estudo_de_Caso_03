import csv
from collections import Counter

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
