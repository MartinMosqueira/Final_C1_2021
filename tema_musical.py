class EmptyError(ValueError):
    pass

class TemaMusical():
    def __init__(self, codigo=None, nombre=None, duracion=0, interprete=None):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete
    
    def __str__(self):
        return 'codigo: '+self.codigo+'\n\tnombre: '+self.nombre+'\n\tduracion: '+str(self.duracion)+'\n\tinterprete: '+self.interprete+'\n'

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,valor):
        if valor == '':
            raise EmptyError('El codigo no puede estar vacio...')
        else:
            self._codigo = valor
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,valor):
        if valor == '':
            raise EmptyError('El nombre no puede estar vacio...')
        else:
            self._nombre = valor
    
    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self,valor):
        if valor < 0:
            raise ValueError('La duracion '+str(valor)+' no puede ser negativa...')
        else:
            self._duracion = valor
    
    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self,valor):
        if valor == '':
            raise EmptyError('El interprete no puede estar vacio...')
        else:
            self._interprete = valor
    
    def input(self,codigo=False):
        if codigo == False:
            key=input('Ingrese Codigo: ')
            self._codigo=key
        nom=input('Ingrese Nombre: ')
        self._nombre=nom
        dur=int(input('Ingrese Duracion: '))
        self._duracion=dur
        inter=input('Ingrese Interprete: ')
        self._interprete=inter
