class Pessoa:
    olhos=2
    def __init__(self,*filhos ,  nome = None, idade = 35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    Renzo = Pessoa(nome='Renzo')
    Luciano = Pessoa(Renzo,nome='Luciano')
    print(Pessoa.cumprimentar(Luciano))
    print(id(Luciano))
    print(Luciano.cumprimentar())
    print(Luciano.nome)
    print(Luciano.idade)
    for filho in Luciano.filhos:
        print(filho.nome)
    del Luciano.filhos
    Luciano.sobrenome = 'Ramalho'
    Luciano.olhos = 1
    del Luciano.olhos
    print(Luciano.__dict__)
    print(Renzo.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(Luciano.olhos)
    print(Renzo.olhos)
    print(id(Pessoa.olhos)), id(Luciano.olhos), id(Renzo.olhos)




