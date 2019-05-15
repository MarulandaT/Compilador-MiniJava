# -*- coding: cp1252 -*-

"""x=10

if x < 5 or (x > 10 and x < 20):
    print "El valor es correcto"
if x < 5 or 10 < x < 20:
    print "El valor es correcto."



while x >= 0:
    print "x todav�a no es negativo."
    x = x - 1

for i in [1,2,3,4,5]:
    print "Iteraci�n no: ", i

for valor in range(100):
    print valor

for milla in range (10, 70, 10):
    km = milla * 1.609
    print "%d millas --> %20.3f kil�metros" % (milla, km)

x = input("Introduzca un numero:")
print x

y = 3
z = 5

nombre = ["Cleese", "Jhon"]
x = [[1,2,3],[y,z],[[[]]]]

print nombre[1], nombre[0]
nombre[0] = "Palin"

print "Esta funci�n crea una lista.


def makelist():
     a = []
     for i in range(1, 20):
         a.append(i)
         print "appending", i, ":", a
     return a

makelist()


x = ["elem0","elem1","elem2","elem3","elem4","huevos","and","elem7"]
print x[5:8]

dicc = { "Alicia" : 23452532, "Boris" : 252336, "Clara" : 2352525 }

print dicc['Alicia']
dicc[53452532] = "aja"

print dicc



def f(x, y):
    x = x + 3
    y.append(23)
    print x, y

x = 22
y = [22]
f(x,y)

print x, y

class Cesta:
    def __init__(self, contenido=[]):
        self.contenido = contenido
    def anadir(self, elemento):
        self.contenido.append(elemento)
    def mostrar(self):
        resultado = ""
        print "Contiene: "
        for elemento in self.contenido:
            print elemento
    def __str__(self):
        resultado = ""
        for elemento in self.contenido:
            resultado = resultado + " " + elemento
        return "Contiene:"+resultado

b = Cesta(['Manzana','Naranja'])
b.mostrar()
print b

def double():
    return x*2

x = 3

print double()

x = 1

print double()

from math import sin, cos

def componer(fun1, fun2):
    def interior(x, fun1 = fun1, fun2 = fun2):
        return fun1(fun2(x))
    return interior

def componer(f1, f2):
    return lambda x, f1 = f1, f2 = f2: f1(f2(x))

sincos = componer(sin, cos)
y = sincos(3)

print y

import string
y="tecoa"
z="Naranja"
x = string.split(y)

print x[0]
print x"""

