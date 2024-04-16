class Triangulo:
    def __init__(self, lados):
        self.lados = lados

    def calcular(self):
        return f"A área é de {self.lados}"
    
if __name__ == "__main__":
    triangulo1 = Triangulo ("3")
    print(triangulo1.lados)