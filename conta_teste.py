from conta import Conta
from conta import Cliente
from conta import Data


data_abertura = Data(9,2,2017)
data_abertura2 = Data(12,3,2020)
cliente = Cliente('Arthur', 'Lola', "70660067471")
cliente2 = Cliente('Gustavo', 'Emanuel', '67668557432')
conta = Conta('1234-0', cliente, 5000, 2000, data_abertura)
conta2 = Conta('5678-0', cliente2, 7000, 4500, data_abertura2)


conta.transfere_para(conta2, 1000)

conta.extrato()
conta2.extrato()

conta.historico.imprime()