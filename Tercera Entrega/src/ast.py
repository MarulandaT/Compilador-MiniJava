#!/usr/bin/python
# -*- coding: utf-8 -*-

cont=0
def incrementarContador():
    global cont 
    cont += 1
    return "%d " % cont


class Node: 
    def __init__(self, tipo, hijos):
      self.hijos = hijos
      self.tipo  = tipo
    
    def imprimir(self, caso):
      print (caso + "   "+ "NT: "+ self.tipo)
      for hijo in self.hijos:
        try:
          hijo.imprimir(caso+"   ")
        except:
          print (caso +"   " + "   " + "T: " + str(hijo))

    def traducir(self):
      self.id =incrementarContador()
      self.txt=""
      for hijo in self.hijos:
        try:
          (x,self.dtxt) = hijo.traducir()
          self.txt += self.id + " -> " + x + "\n\t"
        except:
          self.dtxt = ""
          n=incrementarContador()
          self.txt += self.id + " -> " + n + "\n\t"
          self.txt += n + " [label= "+str(hijo)+"]\n\t"
        self.txt += self.dtxt

      if self.tipo=="PROGRAMA":
        self.txt += self.id + " [label= "+self.tipo+", shape=box, color=red]\n\t"
        return ("digraph G {\n\t"+self.txt+"\n}")
      else:
        self.txt += self.id + " [label= "+self.tipo+"]\n\t"
        return (self.id, self.txt)

      #if self.tipo=="LISTA DECLARACION DE CLASES":
      #  self.id = incrementarContador()
      #  return(self.id, "")

"""
        print ([label= "+self.name+", shape=box])
        for hijo in self.hijos:
          try:
            hijo.traducir()
          except:
            print (caso +"   " + "   " + "T: " + str(hijo))
"""
