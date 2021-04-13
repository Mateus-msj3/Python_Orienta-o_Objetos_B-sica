from conta import Conta
from cliente import Cliente
from historico import Historico

"""
conta = Conta('0001', 'Mateus', 500, 1500)
conta.deposito(200.0)
conta.extrato()
conta.saque(800)
conta.extrato()

"""

cliente_1 = Cliente('Mateus', 'Souza', '000.000.000.00')
cliente_2 = Cliente('Teste', 'Souza', '111.111.111.11')
minha_conta_1 = Conta('0002-1', cliente_1, 120, 1000.0)
minha_conta_2 = Conta('0002-2', cliente_2, 120, 1000.0)
minha_conta_1.deposito(100.0)
minha_conta_1.saque(50.0)
minha_conta_1.transferencia_para(minha_conta_2, 200.0)
minha_conta_1.extrato()
minha_conta_1.historico.imprime()
minha_conta_2.historico.imprime()