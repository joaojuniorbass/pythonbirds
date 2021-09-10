class Pessoa:
    def __init__(self, *filhos, nome = 'João', idade = 38):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self, nome):
        return f"Olá {nome}, eu me chamo {self.nome} e tenho {self.idade} anos de idade"


if __name__ == "__main__":
    joao = Pessoa('Barik', 'Inara')
    io = Pessoa(nome = 'Io - a princesalunar', idade = 22)
    print(io.cumprimentar('Inara'))
    print(joao.cumprimentar('Maldamba'))
    for filho in joao.filhos:
        print(f'Este é o  meu filho {filho}')
    joao.sobrenome = 'Marins'
    del io.filhos
    print(io.__dict__)
    print(joao.__dict__)
