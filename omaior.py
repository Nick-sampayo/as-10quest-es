class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 

    def ligar(self):
        return f"O {self.modelo} está ligando"
    
    def desligar(self):
        return f"O {self.modelo} está desligando"
    
    def acelerar(self):
        return f"O {self.modelo} está acelerando"


if __name__ == "__main__":
    carro1 = Carro("Caoa_Cherry", "Tiggo_5", "2024", "Preto")
    print(carro1.marca, carro1.modelo, carro1.ano, carro1.cor)
    print(carro1.ligar())
    print(carro1.desligar())
    print(carro1.acelerar())
