class Conta:
    def __init__(self, número_da_conta, saldo, titular):
        self.número_da_conta = número_da_conta
        self.saldo = saldo
        self.titular = titular 

    def depositar(self):
        return f"O {self.titular} está depositando o dinheiro"
    
    def sacar(self):
        return f"O {self.titular} está sacando o dinheiro"
    
    def saldo(self):
        return f"O é de {self.saldo}"
    
if __name__ == "__main__":
    conta1 = Conta("26042007", "R$50000000", "Nicolas")
    print(conta1.número_da_conta, conta1.saldo, conta1.titular)
    print(conta1.depositar())
    print(conta1.sacar())
    print(conta1.saldo())