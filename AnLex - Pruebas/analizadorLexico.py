import ply.lex as lex
import re
import codecs

tokens = [
  'ID', 'NUMERO', 'PLUS', 'MINUS', 'POR', 'DIVIDE',
  'MODULO','NEGLOGICA', 'CORCHDER', 'CORCHIZQ','PARENTDER','PARENTIZQ',
  'YAND','OOR','ASIGNAR','MAYORQUE','MENORQUE','ACCESO',
  'MENORIGUAL','MAYORIGUAL','COMPIGUAL','COMPDIFERENTE','FINALIZADOR','LLAVEDER',
  'CADENA','BIN','COMILLASIMPLE','COMA',
  'LLAVEIZQ', 'COMMENT', 'NUMEROC'
]

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

t_ignore = ' \t'
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


##CORREGIR

def t_NUMEROC(t):
	r'(\-)?\d+(\.\d+)?[eE](\-)?\d+'
	#t.value = int(t.value)
	return t

def t_NUMERO(t):
	r'(\-)?\d+'
	#t.value = int(t.value)
	if (int(t.value) < 2147483647 and int(t.value) > -2147483648):
		return t 
	else: 
		t.type="error"
		print(t.value + " esta por fuera del rango del tipo int, en la linea ",  t.lexer.lineno)
	#return t

def t_BIN(t):
	r'b\'[01]+\''
	return t 

def t_CADENA(t):
	r'".*"'
	return t

##SEPARAR NUMEROS DE ID
def t_ID(t):
	r'[a-zA-Z\_]([a-zA-ZÀ-ÿ0-9\_\u00d1\u00f1]*[a-zA-ZÀ-ÿ\_\u00d1\u00f1])?'
	t.value = Reemplazar(t.value)
	t.type = reservadas.get(t.value, 'ID')
	return t

def Reemplazar(palabra):
	identifier = ''
	for i in palabra:
		index = palabra.index(i)
		if (re.search(r'[À-ÿ\u00d1\u00f1]' , i)):
			identifier += '_'
		else:
			identifier += i
	return identifier

# COMENTARIOS DE LA FORMA /* SIN CERRAR SE DEBERIAN CONSIDERAR ERROR
def t_COMMENT(t):
	r'((\/\/[a-zA-Z0-9À-ÿ\u00d1\u00f1\@\(\)\[\]\{\}\,\;\:\_\.\-\t\ ]*)|(\/\*[a-zA-Z0-9À-ÿ\u00d1\u00f1\@\(\)\[\]\{\}\,\;\:\_\.\-\t\n\ ]*\*\/))'
	for i in t.value:
		#index = palabra.index(i)
		if(re.search(r'\n', i)):
			t.lexer.lineno += 1
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print("Caracter incorrecto %s en la linea" (t.value[0], t.lexer.lineno))
	t.lexer.skip(1)



directorio = "test.txt"
fp = codecs.open(directorio,"r","utf-8")
data = fp.read()
fp.close() 

analizador = lex.lex()

"""data ='''
chícheñol
xdxd
'''"""

analizador.input(data)

while True:
	tok = analizador.token()
	if not tok:
		break;
	print(tok)