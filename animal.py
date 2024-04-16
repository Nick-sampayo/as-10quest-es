class Animal:
    def __init__(self, nome, idade, espécie):
        self.nome = nome
        self.idade = idade
        self.espécie = espécie 

    def som(self):
        return f"A {self.nome} está latindo"
    
if __name__ == "__main__":
    animal1 = Animal("Bela", "12", "cachorro")
    print(animal1.nome, animal1.idade, animal1.espécie)
    print(animal1.som())