class Pessoa:
    def __init__(self, nome = None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimenttar(self):
        return f"Olá amigo, me chamo {self.nome}"

if __name__ == "__main__":
    pessoa = Pessoa('João Carlos Marins')
    print(pessoa.cumprimenttar())