from classes.abstractCrud import abstractCrud

class Produto(abstractCrud):
    arquivo = 'db/produto.json'

    def __init__(self, codigo, nome, qtd = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self. qtd = qtd
        self.valor = valor

    