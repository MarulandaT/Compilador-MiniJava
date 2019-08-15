# -*- coding: cp1252 -*-
# Análisis sintáctico
# importa el primer módulo del ply

import ply.yacc as yacc

from calclex import tokens
from astCalc import *



precedence = (
     ('left', 'MAS', 'MENOS'),
     ('left', 'MULT', 'DIVISION'),
 )

def p_statement_assign(p):
    'statement : IDENT IGUAL expression'
    #print("reduce statement : IDENT IGUAL expression")
    p[0]=Statement(p[1], p[3])
    

def p_statement_expr(p):
    'statement : expression'
    #print( 'statement : expression')
    p[0]=p[1]
    print(p[0])

def p_expression_binop(p):
    '''expression : expression MAS expression
                  | expression MENOS expression
                  | expression MULT expression
                  | expression DIVISION expression'''
    #print('reduce statement : expression operador expression')
    p[0]=ExpOp(p[1], p[2], p[3])

        
def p_expression_group(p):
    'expression : PARENIZQ expression PARENDER'
    #print('reduce expression : PARENIZQ expression PARENDER')
    p[0]=ExpGrupo(p[2])

def p_expression_number(p):
    'expression : NUMERO'
    #print( 'reduce expression : NUMERO')
    p[0]=ExpNumero(p[1])
    

def p_expression_name(p):
    'expression : IDENT'
    print('reduce expression : IDENT')

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


yacc.yacc('LALR')
codigoFuente='x1=6*(10-2)'
raiz=yacc.parse(codigoFuente)


print(raiz.evaluar())

