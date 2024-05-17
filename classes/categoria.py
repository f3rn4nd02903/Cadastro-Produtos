from classes.abstractCrud import abstractCrud

class Categoria(abstractCrud):
    arquivo = 'db/categoria.json'
    def __init__(self, nome):
        self.nome = nome

       

