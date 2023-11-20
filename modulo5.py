import csv

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
