class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade 
        self.altura = altura

    def cumprimentar(self):
        return f"{self.nome} está cumprimentando seu amigo"
    
if __name__ == "__main__":
    pessoa1 = Pessoa("Nicolas", "17", "1.88")
    print(pessoa1.nome, pessoa1.idade, pessoa1.altura)
    print(pessoa1.cumprimentar())