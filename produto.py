class Produto:
    def __init__(self, nome, preço, quantidade, estoque):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
        self.estoque = estoque

    def atualizar(self):
        return f"O estoque é de{self.estoque}"
    
    def calcular(self):
        return f"O preço é de {self.preço}"
    
if __name__ == "__main__":
    produto1 = Produto("Banana", "4,00", "500", "0")
    print(produto1.nome, produto1.preço, produto1.quantidade, produto1.estoque)
    print(produto1.atualizar())
    print(produto1.calcular())