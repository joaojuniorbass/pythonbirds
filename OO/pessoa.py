class Pessoa:
    def __init__(self, *filhos, nome = 'João', idade = 38):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self, nome):
        return f"Olá {nome}, eu me chamo {self.nome} e tenho {self.idade} anos de idade"


if __name__ == "__main__":
    pessoa = Pessoa('Pedro', 'Augusta', 'Josué')
    print(pessoa.cumprimentar('Anderson do Molejão'))
    for nome in pessoa.filhos:
        print(f'Um filho se chama {nome}')