import ply.lex as lex
import re
import codecs

#TOKENS
tokens = [
  'ID', 'NUMERO', 'PLUS', 'MINUS', 'POR', 'DIVIDE',
  'MODULO','NEGLOGICA', 'CORCHDER', 'CORCHIZQ','PARENTDER','PARENTIZQ',
  'YAND','OOR','ASIGNAR','MAYORQUE','MENORQUE','ACCESO',
  'MENORIGUAL','MAYORIGUAL','COMPIGUAL','COMPDIFERENTE','FINALIZADOR','LLAVEDER',
  'CADENA','BIN','COMILLASIMPLE','COMA',
  'LLAVEIZQ', 'COMMENT', 'COMMENTLINEA', 'NUMEROC', 'COMILLADOBLE'
]

#PALABRAS RESERVADAS POR MINIJAVA
reservadas = {
	'class':'CLASS',
	'extends': 'EXTENDS',
	'void': 'VOID',
	'int': 'INT',
	'boolean':'BOOLEAN',
	'string': 'STRING',
	'return': 'RETURN',
	'if': 'IF',
	'else': 'ELSE',
	'while': 'WHILE',
	'break': 'BREAK',
	'continue': 'CONTINUE',
	'this':'THIS',
	'new':'NEW',
	'length':'LENGTH',
	'true':'TRUE',
	'false':'FALSE',
	'null':'NULL'
}

tokens += reservadas.values()

#TOKENS UNITARIOS
t_ignore = '[ \t]'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_POR = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'\%'
t_NEGLOGICA = r'\!'
t_CORCHDER = r'\]'
t_CORCHIZQ = r'\['
t_PARENTDER = r'\)'
t_PARENTIZQ = r'\('
t_YAND = r'\&\&'
t_OOR = r'\|\|'
t_ASIGNAR = r'\='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_ACCESO = r'\.'
t_MENORIGUAL = r'\<\='
t_MAYORIGUAL = r'\>\='
t_COMPIGUAL = r'\=\='
t_COMPDIFERENTE = r'\!\='
t_FINALIZADOR = r'\;'
t_LLAVEDER = r'\}'
t_LLAVEIZQ = r'\{'
t_COMILLASIMPLE = r'\''
t_COMA = r'\,'
t_COMILLADOBLE = r'\"'


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


#CIENTIFICO
def t_NUMEROC(t):
	r'(\-)?\d+(\.\d+)?[eE](\-)?\d+'
	t.value = float(t.value)
	return t

#INTS
def t_NUMERO(t):
	r'(\-)?\d+'
	t.value = int(t.value)
	if (int(t.value) < 2147483647 and int(t.value) > -2147483648):
		return t 
	else: 
		t.type="error"
		print(t.value + " esta por fuera del rango del tipo int, en la linea ",  t.lexer.lineno)

#BINARIOS
def t_BIN(t):
	r'b\'[01]+\''
	t.value = t.value[2:]
	t.value = t.value[:-1]
	try:
		t.value = int(t.value, 2)
	except:
		t.value = 0
	return t 

#STRINGS
def t_CADENA(t):
	r'".*"'
	return t

#IDENTIFICADORES
##SEPARAR NUMEROS DE ID
def t_ID(t):
	r'[a-zA-Z\_]([a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\_]*[a-zA-ZáéíóúÁÉÍÓÚñÑ\_])?'
	t.value = Reemplazar(t.value)
	t.type = reservadas.get(t.value, 'ID')
	return t

#REEMPLAZAR CARACTERES ESPECIALES POR _
def Reemplazar(palabra):
	identifier = ''
	for i in palabra:
		if (re.search(r'[áéíóúÁÉÍÓÚñÑ]' , i)):
			identifier += '_'
		else:
			identifier += i
	return identifier

#COMENTARIOS /* */
##COMENTARIOS DE LA FORMA /* SIN CERRAR SE DEBERIAN CONSIDERAR ERROR
def t_COMMENT(t):
	r'((\/\*[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\@\(\)\[\]\{\}\,\;\:\_\.\-\t\ ]*)|(\/\*[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\@\(\)\[\]\{\}\,\;\:\_\.\-\t\n\ ]*\*\/))'
	for i in t.value:
		if(re.search(r'\n', i)):
			t.lexer.lineno += 1

def t_COMMENTLINEA(t):
	r'//.*\n'	
	t.lexer.lineno += 1


#DETECCION DE ERRORES
def t_error(t):
	linea=t.lexer.lineno
	t.value = Reemplazar(t.value)
	print("%s caracter incorrecto en la linea %d" % (t.value[0], linea))
	t.lexer.skip(1)

#INGRESO DE ARCHIVO MINIJAVA
"""
test1 = "test.mj"
test2 = "test2.mj"
test3 = "test3.mj"

opc = int(input("Ingrese el numero de test a realizar: \t"))

if opc == 1:
	directorio = test1;
elif opc == 2: 
	directorio = test2; 
elif opc == 3: 
	directorio = test3;
else:
	directorio = test1;
		
#directorio = "test.mj"
fp = codecs.open(directorio,"r","utf-8")
data = fp.read()
fp.close() """

analizador = lex.lex()

"""
data = '''

'''
"""

#ENTRADA DE TEXTO AL LEXER
"""analizador.input(data)

while True:
	tok = analizador.token()
	if not tok:
		break;
	print(tok) """