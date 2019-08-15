#Segunda Entrega

#!/usr/bin/python
# -*- coding: utf-8 -*-
import ply.lex as lex
import ply.yacc as yacc
from analizadorLexico import tokens
from ast import *

innecesarios = ['{', '}','(',')','.',';',',','=']

# Funcion que va a capturar cada caso segun la produccion para verificar como proceder 
def evaluar(p, tipo):
  hijos = []
  for hijo in p[1:]:
    if hijo not in innecesarios:
      hijos.append(hijo)

  p[0] = Node(tipo, hijos)


precedence =(
             ('right', 'ASIGNAR'),
             ('left', 'OOR'),
             ('left', 'YAND'),
             ('left', 'COMPIGUAL', 'COMPDIFERENTE'),
             ('left', 'MAYORQUE','MENORQUE','MENORIGUAL','MAYORIGUAL'),
             ('left', 'PLUS','MINUS'),
             ('left', 'POR','DIVIDE','MODULO'),
             ('right', 'NEGLOGICA','NEW','UMINUS'),
             ('left', 'CORCHIZQ','CORCHDER','PARENTIZQ','PARENTDER')
            )

#Reglas de la gramatica

def p_PROGRAMA(p):
  '''PROGRAMA : CLASS_DECL_LIST
              | epsilon'''
  evaluar(p, "PROGRAMA")

def p_CLASS_DECL_LIST(p):
  '''CLASS_DECL_LIST : CLASS_DECL
                     | CLASS_DECL CLASS_DECL_LIST'''
  evaluar(p, "LISTA_DECLARACION_DE_CLASES")

def p_CLASS_DECL(p):
  '''CLASS_DECL : CLASS ID EXTENDS ID LLAVEIZQ FIELD_OR_METHOD_DECL_LIST LLAVEDER
                | CLASS ID EXTENDS ID LLAVEIZQ LLAVEDER
                | CLASS ID LLAVEIZQ FIELD_OR_METHOD_DECL_LIST LLAVEDER
                | CLASS ID LLAVEIZQ LLAVEDER '''
  evaluar(p, "DECLARACION_DE_CLASES")
  
def p_FIELD_OR_METHOD_DECL_LIST(p):
  '''FIELD_OR_METHOD_DECL_LIST : FIELD_DECL 
                               | FIELD_DECL FIELD_OR_METHOD_DECL_LIST
                               | METHOD_DECL
                               | METHOD_DECL FIELD_OR_METHOD_DECL_LIST '''
  evaluar(p, "LISTA_DECLARACION_DE_CAMPOS_Y_O_METODOS")
                    
def p_FIELD_DECL(p):
  '''FIELD_DECL : TYPE ID FINALIZADOR
                | TYPE ID LIST_AUX_IDS ';' '''
  evaluar(p, "DECLARACION_DE_CAMPO")
  
def p_LIST_AUX_IDS(p):
  '''LIST_AUX_IDS : COMA ID 
                  | COMA ID LIST_AUX_IDS'''
  evaluar(p, "LISTA_AUXILIAR_DE_IDS")

def p_METHOD_DECL(p):
  '''METHOD_DECL : TYPE ID PARENTIZQ PARENTDER BLOCK
                 | TYPE ID PARENTIZQ FORMALS PARENTDER BLOCK
                 | VOID ID PARENTIZQ PARENTDER BLOCK
                 | VOID ID PARENTIZQ FORMALS PARENTDER BLOCK'''
  evaluar(p, "DECLARACION_DE_METODO")
  
def p_FORMALS(p):
  '''FORMALS : TYPE ID
             | TYPE ID COMA FORMALS '''
  evaluar(p, "FORMALS")
                       
def p_TYPE(p):
  '''TYPE : INT 
          | BOOLEAN 
          | STRING 
          | ID 
          | TYPE CORCHIZQ CORCHDER '''
  evaluar(p, "TIPO")

def p_BLOCK(p):
  '''BLOCK : LLAVEIZQ LLAVEDER
           | LLAVEIZQ VAR_DECL_STATEMENTS_LIST LLAVEDER '''
  evaluar(p, "BLOQUE")
  
def p_VAR_DECL_STATEMENTS_LIST(p):
  '''VAR_DECL_STATEMENTS_LIST :  VAR_DECL
                              |  VAR_DECL VAR_DECL_STATEMENTS_LIST
                              |  STATEMENT
                              |  STATEMENT VAR_DECL_STATEMENTS_LIST'''
  evaluar(p, "LISTA_DE_VAR_DECL_Y_ENUNCIADOS") 


def p_VAR_DECL(p):
  '''VAR_DECL : TYPE ID LIST_IDS_EXPRESSIONS FINALIZADOR
              | TYPE ID FINALIZADOR 
              | TYPE ID ASIGNAR EXPRESSION LIST_IDS_EXPRESSIONS FINALIZADOR
              | TYPE ID ASIGNAR EXPRESSION FINALIZADOR '''
  evaluar(p, "DECLARACION_DE_VARIABLE")

def p_LIST_IDS_EXPRESSIONS(p):
  '''LIST_IDS_EXPRESSIONS : COMA ID
                          | COMA ID ASIGNAR EXPRESSION
                          | COMA ID LIST_IDS_EXPRESSIONS
                          | COMA ID ASIGNAR EXPRESSION LIST_IDS_EXPRESSIONS '''
  evaluar(p, "LISTA_DE_IDS_Y_EXPRESIONES")
                          

def p_STATEMENT(p):
  '''STATEMENT : ASSIGN FINALIZADOR
               | CALL FINALIZADOR
               | RETURN EXPRESSION FINALIZADOR
               | RETURN FINALIZADOR
               | IF PARENTIZQ EXPRESSION PARENTDER STATEMENT ELSE STATEMENT
               | IF PARENTIZQ EXPRESSION PARENTDER STATEMENT
               | WHILE PARENTIZQ EXPRESSION PARENTDER STATEMENT
               | BREAK FINALIZADOR
               | CONTINUE FINALIZADOR
               | BLOCK '''
  evaluar(p, "ENUNCIADO")
  
def p_ASSIGN(p):
  '''ASSIGN : LOCATION ASIGNAR EXPRESSION'''
  evaluar(p, "ASIGNACION")
  
def p_LOCATION(p):
  '''LOCATION : ID
              | EXPRESSION ACCESO ID
              | ID CORCHIZQ EXPRESSION CORCHDER '''
  evaluar(p, "LOCACION")
  
def p_CALL(p):
  '''CALL : METHOD PARENTIZQ ACTUALS PARENTDER
          | METHOD PARENTIZQ PARENTDER ''' 
  evaluar(p, "LLAMADA")
  
def p_METHOD(p):
  '''METHOD : ID
            | EXPRESSION ACCESO ID '''
  evaluar(p, "METODO")

def p_ACTUALS(p):
  '''ACTUALS : EXPRESSION
             | EXPRESSION COMA ACTUALS '''
  evaluar(p, "ACTUALS")
  
def p_EXPRESSION(p):
  '''EXPRESSION : LOCATION
                | CALL
                | THIS
                | NEW ID PARENTIZQ PARENTDER
                | NEW TYPE CORCHIZQ EXPRESSION CORCHDER
                | EXPRESSION ACCESO LENGTH
                | BINARY_EXPRESSION
                | NEGLOGICA EXPRESSION
                | MINUS EXPRESSION %prec UMINUS
                | LITERAL
                | PARENTIZQ EXPRESSION PARENTDER '''
  evaluar(p, "EXPRESION")

def p_BINARY(p):
  '''BINARY_EXPRESSION : EXPRESSION PLUS EXPRESSION
                       | EXPRESSION MINUS EXPRESSION
                       | EXPRESSION POR EXPRESSION
                       | EXPRESSION DIVIDE EXPRESSION
                       | EXPRESSION MODULO EXPRESSION
                       | EXPRESSION YAND EXPRESSION
                       | EXPRESSION OOR EXPRESSION
                       | EXPRESSION MENORQUE EXPRESSION
                       | EXPRESSION MENORIGUAL EXPRESSION
                       | EXPRESSION MAYORQUE EXPRESSION
                       | EXPRESSION MAYORIGUAL EXPRESSION
                       | EXPRESSION COMPIGUAL EXPRESSION
                       | EXPRESSION COMPDIFERENTE EXPRESSION '''
  evaluar(p, "EXPRESION_BINARIA")

def p_LITERAL(p):
  '''LITERAL : NUMERO
             | BIN
             | NUMEROC
             | CADENA
             | TRUE
             | FALSE
             | NULL '''
  evaluar(p, "LITERAL")

def p_epsilon(p):
  'epsilon :'
  pass
  

def p_error(p):
  print("Error de sintaxis en el token '"+ str(p.value) +"' que aparece en la "+
        "linea numero "+ str(p.lineno))

# Generar la tabla de analisis sintactico

yacc.yacc('LALR')

parser = yacc.yacc()


test = {'1' : 'quickSortMiniJava.txt',
        '2' : 'PruebaCorrecta.txt',
        '3' : 'PruebaIncorrecta.txt',
        '4' : 'vacio.txt'}

opcionElegida = ""

print("\nAnalizador sintactico de MiniJava")
print("Escoja una opcion: ")
print("1. quicksort")
print("2. Prueba sintacticamente correcta ")
print("3. prueba incorrecta")
print("4. archivo vacio")

opcionElegida= input()
if(opcionElegida in test):
    codigoFuente = open('../test/'+test[opcionElegida], 'r').read()
    print(parser.parse(codigoFuente).traducir())
    
elif (opcionElegida != "-1"):
    print("\nPor favor digite una opcion valida\n")  

