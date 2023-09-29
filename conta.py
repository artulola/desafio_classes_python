import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def imprime(self):
        print("Data abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)


class Cliente:
    
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Conta:
    
    def __init__(self, numero, cliente, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if(valor > self.saldo):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True

    def extrato(self):
        print('Nome: {} \nSobrenome: {} \nCPF: {} \nNúmero: {} \nData de criação: {}/{}/{} \nSaldo: {}'.format(self.titular.nome, self.titular.sobrenome, self.titular.cpf, self.numero, self.data_abertura.dia, self.data_abertura.mes, self.data_abertura.ano, self.saldo))
        print("----------------------------")
        self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferência de {} para conta {}".format(valor, destino))
            return True