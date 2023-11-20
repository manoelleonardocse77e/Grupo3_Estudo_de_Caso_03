import csv

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