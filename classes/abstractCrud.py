import json

class abstractCrud:
    def detalhar(self):
          return self.__dict__
     
    def inserir(self):
          
        lista = self.consultar()

        lista.append(self.detalhar()) #adiciona o detalhar a lista
        with open(self.arquivo, 'w') as file:
             lista = json.dump(lista, file, indent= 4)
        
    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f'{i} - {p}')

    @classmethod      #metodo de classe, chamado por cls
    def consultar(cls):
        try: #Tenta executar o codigo do bloco
            with open(cls.arquivo) as file: #abre o arquivo json
                return json.load(file) #carrega o conteudo do arquivo 
        except Exception: #trata possiveis erros, exemplo caso o arquivo json estiver vazio
            return []         

print('Registrado com sucesso!')     
