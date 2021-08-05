class ListaMusical():
    def __init__(self,temas=None):
        self.temas = dict()
    
    def add(self, tema):
        if tema.codigo in self.temas:
            raise KeyError('El codigo '+tema.codigo +' ya existe...')
        else:
            self.temas[tema.codigo]=tema
    
    def update(self, tema, key):
        if key in self.temas:
            self.temas[key]=tema
        else:
            raise KeyError('El codigo '+key+' no existe...')
    
    def delete(self, key):
        if key in self.temas:
            del self.temas[key]
        else:
            raise KeyError('El codigo '+key+' no existe...')
    
    def find_by_id(self, key):
        if key in self.temas:
            return self.temas[key]
        else:
            raise KeyError('El codigo '+key+' no existe...')
    
    def find_all(self):
        lista=[]
        for tema in self.temas:
            lista.append(self.temas[tema])
        return lista
