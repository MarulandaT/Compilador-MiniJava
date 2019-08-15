import ply.yacc as yacc 

import re 
from src import tokens 
from astCalc import *





def p_program(p):
	'program : programprim'
	print ("1")

def p_programp(p):
	'''programprim : classdecl programprim
				   | 
	'''

	print ("2")

def p_classdecl(p):
	'classdecl : CLASS ID A LLAVEIZQ B LLAVEDER'
	print ("3")

def p_herencia(p):
	'''A : EXTENDS ID
		 | 
	'''
	print ("4")

def p_contprograma(p):
	'''B : fielddecl B
		 | methdecl B
		 | 
	'''
	print ("5")

def p_field(p):
	'fielddecl : TYPE ID C FINALIZADOR' 
	print ("6")

def p_declaracionopcional(p):
	'''C : COMA ID C
		 |
	'''
	print ("7")

def p_methdecl(p):   
	'methdecl : D ID  PARENTIZQ E PARENTDER block'
	print ("8")

def p_pdecltipo(p):
	'''D : TYPE
		 | VOID'''
	print ("9")

def p_declcontent(p):
	'''E : formals
		 |
	'''
	print ("10")

def p_formals(p):
	'formals : TYPE ID F'
	print ("11")

def p_formalscontent(p):
	'''F : COMA TYPE ID F
		 | 
	'''
	print ("12")

def p_typespecs(p):
	'TYPE : G'
	print ("13")

def p_typespecint(p):
	'''G : INT
		 | BOOLEAN
		 | STRING
		 | ID
		 | TYPE CORCHIZQ CORCHDER
	'''
	print ("14")

def p_block(p):
	'block : LLAVEIZQ H I LLAVEDER'
	print ("15")

def p_vardeclH(p):
	'''H : vardecl H
		 | 
	'''
	print ("16")

def p_stmtI(p):
	'''I : stmt I
		 | 
	'''
	print ("17")

def p_vardecl(p):
	'vardecl : TYPE ID J L FINALIZADOR'
	print ("18") 

def p_vardeclJ(p):
	'''J : ASIGNAR expr
		 |
	'''
	print ("19")

def p_vardeclk(p):
	'K : COMA ID J'
	print ("20")

def p_vardecll(p):
	'''L : K L
		 |
	'''
	print ("21")

def p_stmt(p):
	'stmt : M'
	print ("22")

def p_stmtmas(p):
	'''M : assign FINALIZADOR
		 | call FINALIZADOR
		 | RETURN N
		 | IF PARENTIZQ expr PARENTDER stmt O
		 | WHILE PARENTIZQ expr PARENTDER stmt
		 | BREAK FINALIZADOR
		 | CONTINUE FINALIZADOR
		 | block
	'''
	print ("23")

def p_stmtmreturnn(p):
	'''N : expr
		 | 
	'''
	print ("24")

def p_stmtmifo(p):
	'''O : ELSE stmt
		 |
	'''
	print ("25")

def p_assign(p):
	'assign : location ASIGNAR expr'
	print ("26")

def p_locationPprima(p):
	'''location : method'''
	print ("27")

def p_locationPPrima(p):
	'location : Pprima'
	print ("28")

def p_method(p):
	'method : P'
	print ("29")

def p_locationpid(p):
	'''P : ID
		 | expr ACCESO ID
	'''
	print ("30")

def p_locationpexprexpr(p):
	'Pprima : expr CORCHIZQ expr CORCHDER'
	print ("31")

def p_call(p):
	'call : method PARENTIZQ Q PARENTDER'
	print ("32")

def p_callQ(p):
	'''Q : actuals
		 | 
	'''
	print ("33")

def p_actuals(p):
	'actuals : expr S'
	print ("34")

def p_actualsS(p):
	'''S : expr S
		 | 
	'''
	print ("35")


def p_expr(p):
	'expr : T'
	print ("36")

def p_Tlocation(p):
	'''T : location
		 | call
		 | THIS
		 | NEW ID PARENTIZQ PARENTDER
		 | NEW TYPE CORCHIZQ expr CORCHDER
		 | expr ACCESO LENGTH
		 | expr binary expr
		 | unary expr
		 | literal
		 | PARENTIZQ expr PARENTDER
	'''
	print ("37")


def p_binary(p):
	'binary : U'
	print ("38")

def p_Uresiduo(p):
	'''U : MODULO
		 | YAND
		 | OOR
		 | MENORQUE
		 | MENORIGUAL
		 | MAYORQUE
		 | MAYORIGUAL 
		 | COMPIGUAL
		 | COMPDIFERENTE
		 | PLUS
		 | MINUS
		 | POR 
		 | DIVIDE
	'''
	print ("39")

def p_unarydiferente(p):
	'unary : NEGLOGICA'
	print ("40")

def p_literal(p):
	'literal : V'
	print ("41")

def p_V(p):
	'''V : NUMERO 
		 | CADENA 
		 | TRUE
		 | FALSE
		 | NULL
	'''
	print ("42")

def p_error(p):
	print("Error de sintaxis en '%s'" % p.value)
	#print("No se reconoce el caracter '%s' de la linea %d" %(p.value[0], p.lineno))

yacc.yacc('LALR')
codigoFuente='''
class prueba extends Ri {
	int  x,z,s ;
	
	void method() {
		int m=1;
	}

	void y() {
		int x = z+s;
		int z = y + h; 
		if ( x == 3 ) { }	
	}
	
}


class Test {
  int partition(int [] a, int low, int high) {
      int i = low;
      quicksort(a, low, mid);
      //quicksort(a, mid+1, high);
      return j;
  }
}


'''
raiz = yacc.parse(codigoFuente)

print (raiz)