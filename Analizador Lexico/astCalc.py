class Nodo:
	pass


class Node: 
    def __init__(self, nombre, hijos=None, hoja=None):
        self.nombre = nombre
        if hijos == None:
            hijos = []

        self.hijos = [x for x in hijos if x!=None]

        self.hoja = hoja

    def append(self, Nodo):
        self.hijos.append(Nodo)

    def __str__(self):
        return '<%s>' %(self.nombre)