from historico import Historico

class Conta:

    # Inicializador da classe
    def __init__(self, numero, titular, saldo, limite = 1500.0):
        print('Inicializando uma conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    # Metodo de depósito
    def deposito(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor} R$')

    # Metodo de saque
    def saque(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de {valor} R$')
            return True
    
    # Metodo de transferencia
    def transferencia_para(self, destino, valor):
        retirou_valor = self.saque(valor)
        if(retirou_valor == False):
            return False
        else:
            destino.deposito(valor)
            self.historico.transacoes.append(f'Transferência de {valor} para a conta {destino.numero}')
            return True
    

    # Metodo de extrato, ou informações da conta
    def extrato(self):
        print(f'Numero da Conta: {self.numero} \nSaldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou o extrato - saldo de {self.saldo}')