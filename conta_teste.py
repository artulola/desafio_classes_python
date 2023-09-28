from conta import Conta

conta = Conta('1234-0', 'Lola', 5000, 2000 )
conta2 = Conta('5678-0', 'Gustavo', 7000, 4500)

conta.transfere_para(conta2, 1000)

conta.extrato()
conta2.extrato()