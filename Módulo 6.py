import csv

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