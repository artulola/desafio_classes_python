class Cliente:
    
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf



class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(valor > self.saldo):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print('Número: {} \nSaldo: {}'.format(self.numero, self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True