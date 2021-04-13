import datetime

class Historico():

    def __init__(self):
        self.data_de_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def imprime(self):
        print(f'Data de abertura: {self.data_de_abertura}')
        print('Transações')
        for t in self.transacoes:
            print('-', t)