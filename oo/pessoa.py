class Pessoa:
    olhos=2
    def __init__(self,*filhos ,  nome = None, idade = 35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class homem(Pessoa):
    pass

if __name__ == '__main__':
    Renzo = homem(nome='Renzo')
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
    print(id(Pessoa.olhos), id(Luciano.olhos), id(Renzo.olhos))
    print(Pessoa.metodo_estatico() , Luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe() , Luciano.nome_e_atributos_de_classe())
    pessoaAnonima = Pessoa('Anonimo')
    print(isinstance(pessoaAnonima, Pessoa))
    print(isinstance(pessoaAnonima, homem))
    print(isinstance(Renzo, homem))
    print(isinstance(Renzo, Pessoa))






