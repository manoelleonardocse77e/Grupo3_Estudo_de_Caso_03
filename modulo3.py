import csv

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
