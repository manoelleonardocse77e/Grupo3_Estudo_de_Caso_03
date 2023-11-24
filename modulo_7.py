import csv

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
