# -*- coding: cp1252 -*-
# ------------------------------------------------------------
 # calclex.py
 #
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------
import ply.lex as lex
 
 # List of token names.   This is always required
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'LCORCH',
'DCORCH',
'IDENTIFICADOR',
'IGUAL',
'CADENA',
'COMMENT',
'BCOMMENT',
'CMMUNGUION',
'NUMERAL',
'PMAL'
)

# Regular expression rules for simple tokens
t_PLUS              = r'\+'
t_MINUS             = r'\-'
t_TIMES             = r'\*'
t_DIVIDE            = r'\/'
t_LPAREN            = r'\('
t_RPAREN            = r'\)'
t_LCORCH            = r'\['
t_DCORCH            = r'\]'
t_IDENTIFICADOR     = r'[a-zA-z0-9]+'
t_IGUAL             = r'\='
t_CADENA            = r'\".*\"'
t_COMMENT           = r'\/\*(.|\n)*\*\/'
t_BCOMMENT          = r'\/\/.*'
t_CMMUNGUION        = r'[a-zA-Z][a-zA-Z0-9]*\_{1}[a-zA-Z0-9]*$'
t_NUMERAL           = r'\#\#(.|\n)*\#\#'
t_PMAL              = r'http://paginamal.al.co'

 
 
    

# A regular expression rule with some action code
def t_NUMBER(t):
 r'\d+'
 t.value = int(t.value)
 return t

    

# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
#t_ignore_COMENTARIO = r'//'

# Error handling rule
def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

# Build the lexer
analizador = lex.lex()


#To use the lexer, you first need to feed it some input text using its input() method. 
#After that, repeated calls to token() produce tokens. The following code shows how this works:


# Test it out
data = '''
 /*Santa
 a ver
 pelien */

 aA098_3189

 ##Santa
 a ver
 ese ##
 
'''

# Give the lexer some input
analizador.input(data)

# Tokenize
while True:
 tok = analizador.token()
 if not tok: 
     break      # No more input
 print(tok)
