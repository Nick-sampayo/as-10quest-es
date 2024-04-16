class Livro: 
    def __init__(self, título, autor, páginas):
        self.título = título
        self.autor = autor
        self.páginas = páginas

    def informações(self):
        return f"O {self.título} é de comédia romântica"
    
    def quantidade(self):
        return f"A quantidade páginas {self.páginas}"
    
if __name__ == "__main__":
    livro1 = Livro("Perdidos em Recife", "Nicolas Sampaio", "325")
    print(livro1.título, livro1.autor, livro1.páginas)
    print(livro1.informações())
    print(livro1.quantidade())