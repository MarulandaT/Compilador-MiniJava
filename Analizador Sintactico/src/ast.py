#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node: 
    def __init__(self, hijos, tipo):
      self.hijos = hijos
      self.tipo  = tipo
    
    def imprimir(self, caso):
      print (caso + "   "+ "NT: "+ self.tipo)
      for hijo in self.hijos:
        try:
          hijo.imprimir(caso+"   ")
        except:
          print (caso +"   " + "   " + "T: " + str(hijo))
