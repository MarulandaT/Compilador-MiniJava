
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCESO ASIGNAR BIN BOOLEAN BREAK CADENA CLASS COMA COMILLADOBLE COMILLASIMPLE COMMENT COMPDIFERENTE COMPIGUAL CONTINUE CORCHDER CORCHIZQ DIVIDE ELSE EXTENDS FALSE FINALIZADOR ID IF INT LENGTH LLAVEDER LLAVEIZQ MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MINUS MODULO NEGLOGICA NEW NULL NUMERO NUMEROC OOR PARENTDER PARENTIZQ PLUS POR RETURN STRING THIS TRUE VOID WHILE YANDprogram : programprimprogramprim : classdecl programprim\n\t\t\t\t   | \n\tclassdecl : CLASS ID A LLAVEIZQ B LLAVEDERA : EXTENDS ID\n\t\t | \n\tB : fielddecl B\n\t\t | methdecl B\n\t\t | \n\tfielddecl : TYPE ID C FINALIZADORC : COMA ID C\n\t\t |\n\tmethdecl : D ID  PARENTIZQ E PARENTDER blockD : TYPE\n\t\t | VOIDE : formals\n\t\t |\n\tformals : TYPE ID FF : COMA TYPE ID F\n\t\t | \n\tTYPE : GG : INT\n\t\t | BOOLEAN\n\t\t | STRING\n\t\t | ID\n\t\t | TYPE CORCHIZQ CORCHDER\n\tblock : LLAVEIZQ H I LLAVEDERH : vardecl H\n\t\t | \n\tI : stmt I\n\t\t | \n\tvardecl : TYPE ID J L FINALIZADORJ : ASIGNAR expr\n\t\t |\n\tK : COMA ID JL : K L\n\t\t |\n\tstmt : MM : assign FINALIZADOR\n\t\t | call FINALIZADOR\n\t\t | RETURN N\n\t\t | IF PARENTIZQ expr PARENTDER stmt O\n\t\t | WHILE PARENTIZQ expr PARENTDER stmt\n\t\t | BREAK FINALIZADOR\n\t\t | CONTINUE FINALIZADOR\n\t\t | block\n\tN : expr\n\t\t | \n\tO : ELSE stmt\n\t\t |\n\tassign : location ASIGNAR exprlocation : methodlocation : Pprimamethod : PP : ID\n\t\t | expr ACCESO ID\n\tPprima : expr CORCHIZQ expr CORCHDERcall : method PARENTIZQ Q PARENTDERQ : actuals\n\t\t | \n\tactuals : expr SS : expr S\n\t\t | \n\texpr : TT : location\n\t\t | call\n\t\t | THIS\n\t\t | NEW ID PARENTIZQ PARENTDER\n\t\t | NEW TYPE CORCHIZQ expr CORCHDER\n\t\t | expr ACCESO LENGTH\n\t\t | expr binary expr\n\t\t | unary expr\n\t\t | literal\n\t\t | PARENTIZQ expr PARENTDER\n\tbinary : UU : MODULO\n\t\t | YAND\n\t\t | OOR\n\t\t | MENORQUE\n\t\t | MENORIGUAL\n\t\t | MAYORQUE\n\t\t | MAYORIGUAL \n\t\t | COMPIGUAL\n\t\t | COMPDIFERENTE\n\t\t | PLUS\n\t\t | MINUS\n\t\t | POR \n\t\t | DIVIDE\n\tunary : NEGLOGICAliteral : VV : NUMERO \n\t\t | CADENA \n\t\t | TRUE\n\t\t | FALSE\n\t\t | NULL\n\t'
    
_lr_action_items = {'$end':([0,1,2,3,5,22,],[-3,0,-1,-3,-2,-4,]),'CLASS':([0,3,22,],[4,4,-4,]),'ID':([4,8,9,11,13,14,15,16,17,18,19,20,21,29,30,31,32,36,40,41,43,44,45,46,47,49,50,53,55,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,120,122,124,125,126,131,133,136,138,139,140,141,142,144,146,149,150,152,154,155,156,],[6,10,11,-25,11,11,25,27,-21,-15,-22,-23,-24,33,-26,11,-10,39,-13,11,11,65,11,79,80,65,-38,65,65,-46,-53,-54,-55,-64,-67,114,65,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,65,65,124,65,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,65,-44,-45,65,65,-72,65,124,-74,-56,-70,-71,65,65,148,65,-57,65,-58,65,-68,-32,-50,-43,-69,-42,65,-49,]),'EXTENDS':([6,],[8,]),'LLAVEIZQ':([6,7,10,38,41,44,45,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,138,139,140,141,144,146,149,150,152,154,155,156,],[-6,9,-5,41,-29,41,-29,41,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,41,-57,41,-58,-68,-32,-50,-43,-69,-42,41,-49,]),'LLAVEDER':([9,12,13,14,23,24,32,40,41,44,45,48,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,82,83,84,85,86,87,88,89,110,111,116,122,124,125,126,139,141,144,146,149,150,152,154,156,],[-9,22,-9,-9,-7,-8,-10,-13,-29,-31,-29,81,-31,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-30,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,-57,-58,-68,-32,-50,-43,-69,-42,-49,]),'VOID':([9,13,14,32,40,81,],[18,18,18,-10,-13,-27,]),'INT':([9,13,14,31,32,40,41,43,45,68,81,146,],[19,19,19,19,-10,-13,19,19,19,19,-27,-32,]),'BOOLEAN':([9,13,14,31,32,40,41,43,45,68,81,146,],[20,20,20,20,-10,-13,20,20,20,20,-27,-32,]),'STRING':([9,13,14,31,32,40,41,43,45,68,81,146,],[21,21,21,21,-10,-13,21,21,21,21,-27,-32,]),'CORCHIZQ':([11,15,17,19,20,21,30,36,46,47,52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,114,115,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-25,26,-21,-22,-23,-24,-26,26,26,26,-66,92,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,92,-65,-66,-52,92,-25,133,92,92,-74,92,-56,-70,92,92,92,92,92,-57,-58,92,-68,92,-69,]),'COMA':([25,33,39,63,64,65,66,67,70,72,73,74,75,76,77,79,80,87,88,89,116,117,122,124,125,126,135,137,139,141,144,148,152,153,],[29,29,43,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-34,43,-65,-66,-52,-72,136,-74,-56,-70,-71,136,-33,-57,-58,-68,-34,-69,-35,]),'FINALIZADOR':([25,28,33,37,51,52,58,59,63,64,65,66,67,70,72,73,74,75,76,77,79,87,88,89,116,117,122,124,125,126,128,134,135,137,139,141,144,147,148,152,153,],[-12,32,-12,-11,83,84,110,111,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-34,-65,-66,-52,-72,-37,-74,-56,-70,-71,-51,146,-37,-33,-57,-58,-68,-36,-34,-69,-35,]),'CORCHDER':([26,63,64,65,66,67,70,72,73,74,75,76,77,87,88,89,116,122,123,124,125,126,133,139,141,144,145,152,],[30,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-65,-66,-52,-72,-74,139,-56,-70,-71,30,-57,-58,-68,152,-69,]),'PARENTIZQ':([27,41,44,45,49,50,53,54,55,57,60,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[31,-29,55,-29,55,-38,55,90,55,109,-46,113,-53,-54,-55,-64,-67,55,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,113,55,55,55,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,55,-44,-45,55,55,132,-72,55,-74,-56,-70,-71,55,55,55,-57,55,-58,55,-68,-32,-50,-43,-69,-42,55,-49,]),'PARENTDER':([31,34,35,39,42,63,64,65,66,67,70,72,73,74,75,76,77,80,87,88,89,91,113,116,119,121,122,124,125,126,127,129,130,131,132,139,141,142,143,144,151,152,],[-17,38,-16,-20,-18,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-20,-65,-66,-52,122,-60,-72,-19,138,-74,-56,-70,-71,140,141,-59,-63,144,-57,-58,-63,-61,-68,-62,-69,]),'RETURN':([41,44,45,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,138,139,140,141,144,146,149,150,152,154,155,156,],[-29,53,-29,53,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,53,-57,53,-58,-68,-32,-50,-43,-69,-42,53,-49,]),'IF':([41,44,45,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,138,139,140,141,144,146,149,150,152,154,155,156,],[-29,54,-29,54,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,54,-57,54,-58,-68,-32,-50,-43,-69,-42,54,-49,]),'WHILE':([41,44,45,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,138,139,140,141,144,146,149,150,152,154,155,156,],[-29,57,-29,57,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,57,-57,57,-58,-68,-32,-50,-43,-69,-42,57,-49,]),'BREAK':([41,44,45,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,138,139,140,141,144,146,149,150,152,154,155,156,],[-29,58,-29,58,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,58,-57,58,-58,-68,-32,-50,-43,-69,-42,58,-49,]),'CONTINUE':([41,44,45,49,50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,138,139,140,141,144,146,149,150,152,154,155,156,],[-29,59,-29,59,-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,59,-57,59,-58,-68,-32,-50,-43,-69,-42,59,-49,]),'THIS':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,67,-29,67,-38,67,67,-46,-53,-54,-55,-64,-67,67,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,67,67,67,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,67,-44,-45,67,67,-72,67,-74,-56,-70,-71,67,67,67,-57,67,-58,67,-68,-32,-50,-43,-69,-42,67,-49,]),'NEW':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,68,-29,68,-38,68,68,-46,-53,-54,-55,-64,-67,68,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,68,68,68,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,68,-44,-45,68,68,-72,68,-74,-56,-70,-71,68,68,68,-57,68,-58,68,-68,-32,-50,-43,-69,-42,68,-49,]),'NEGLOGICA':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,71,-29,71,-38,71,71,-46,-53,-54,-55,-64,-67,71,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,71,71,71,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,71,-44,-45,71,71,-72,71,-74,-56,-70,-71,71,71,71,-57,71,-58,71,-68,-32,-50,-43,-69,-42,71,-49,]),'NUMERO':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,73,-29,73,-38,73,73,-46,-53,-54,-55,-64,-67,73,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,73,73,73,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,73,-44,-45,73,73,-72,73,-74,-56,-70,-71,73,73,73,-57,73,-58,73,-68,-32,-50,-43,-69,-42,73,-49,]),'CADENA':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,74,-29,74,-38,74,74,-46,-53,-54,-55,-64,-67,74,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,74,74,74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,74,-44,-45,74,74,-72,74,-74,-56,-70,-71,74,74,74,-57,74,-58,74,-68,-32,-50,-43,-69,-42,74,-49,]),'TRUE':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,75,-29,75,-38,75,75,-46,-53,-54,-55,-64,-67,75,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,75,75,75,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,75,-44,-45,75,75,-72,75,-74,-56,-70,-71,75,75,75,-57,75,-58,75,-68,-32,-50,-43,-69,-42,75,-49,]),'FALSE':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,76,-29,76,-38,76,76,-46,-53,-54,-55,-64,-67,76,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,76,76,76,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,76,-44,-45,76,76,-72,76,-74,-56,-70,-71,76,76,76,-57,76,-58,76,-68,-32,-50,-43,-69,-42,76,-49,]),'NULL':([41,44,45,49,50,53,55,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,118,122,124,125,126,131,133,138,139,140,141,142,144,146,149,150,152,154,155,156,],[-29,77,-29,77,-38,77,77,-46,-53,-54,-55,-64,-67,77,-73,-89,-90,-91,-92,-93,-94,-95,-28,-27,-39,-40,-41,-47,-65,-66,-52,77,77,77,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,77,-44,-45,77,77,-72,77,-74,-56,-70,-71,77,77,77,-57,77,-58,77,-68,-32,-50,-43,-69,-42,77,-49,]),'ELSE':([50,53,60,63,64,65,66,67,70,72,73,74,75,76,77,81,83,84,85,86,87,88,89,110,111,116,122,124,125,126,139,141,144,149,150,152,154,156,],[-38,-48,-46,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,-27,-39,-40,-41,-47,-65,-66,-52,-44,-45,-72,-74,-56,-70,-71,-57,-58,-68,155,-43,-69,-42,-49,]),'ACCESO':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,93,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,120,-65,-66,-52,120,120,120,-74,120,-56,-70,120,120,120,120,120,-57,-58,120,-68,120,-69,]),'MODULO':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,96,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,96,-65,-66,-52,96,96,96,-74,96,-56,-70,96,96,96,96,96,-57,-58,96,-68,96,-69,]),'YAND':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,97,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,97,-65,-66,-52,97,97,97,-74,97,-56,-70,97,97,97,97,97,-57,-58,97,-68,97,-69,]),'OOR':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,98,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,98,-65,-66,-52,98,98,98,-74,98,-56,-70,98,98,98,98,98,-57,-58,98,-68,98,-69,]),'MENORQUE':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,99,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,99,-65,-66,-52,99,99,99,-74,99,-56,-70,99,99,99,99,99,-57,-58,99,-68,99,-69,]),'MENORIGUAL':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,100,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,100,-65,-66,-52,100,100,100,-74,100,-56,-70,100,100,100,100,100,-57,-58,100,-68,100,-69,]),'MAYORQUE':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,101,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,101,-65,-66,-52,101,101,101,-74,101,-56,-70,101,101,101,101,101,-57,-58,101,-68,101,-69,]),'MAYORIGUAL':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,102,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,102,-65,-66,-52,102,102,102,-74,102,-56,-70,102,102,102,102,102,-57,-58,102,-68,102,-69,]),'COMPIGUAL':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,103,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,103,-65,-66,-52,103,103,103,-74,103,-56,-70,103,103,103,103,103,-57,-58,103,-68,103,-69,]),'COMPDIFERENTE':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,104,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,104,-65,-66,-52,104,104,104,-74,104,-56,-70,104,104,104,104,104,-57,-58,104,-68,104,-69,]),'PLUS':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,105,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,105,-65,-66,-52,105,105,105,-74,105,-56,-70,105,105,105,105,105,-57,-58,105,-68,105,-69,]),'MINUS':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,106,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,106,-65,-66,-52,106,106,106,-74,106,-56,-70,106,106,106,106,106,-57,-58,106,-68,106,-69,]),'POR':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,107,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,107,-65,-66,-52,107,107,107,-74,107,-56,-70,107,107,107,107,107,-57,-58,107,-68,107,-69,]),'DIVIDE':([52,56,61,62,63,64,65,66,67,70,72,73,74,75,76,77,86,87,88,89,91,116,121,122,123,124,125,126,127,128,131,137,139,141,142,144,145,152,],[-66,108,-65,-52,-53,-54,-55,-64,-67,-73,-90,-91,-92,-93,-94,-95,108,-65,-66,-52,108,108,108,-74,108,-56,-70,108,108,108,108,108,-57,-58,108,-68,108,-69,]),'ASIGNAR':([61,62,63,64,65,79,124,139,148,],[112,-52,-53,-54,-55,118,-56,-57,118,]),'LENGTH':([93,120,],[125,125,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'programprim':([0,3,],[2,5,]),'classdecl':([0,3,],[3,3,]),'A':([6,],[7,]),'B':([9,13,14,],[12,23,24,]),'fielddecl':([9,13,14,],[13,13,13,]),'methdecl':([9,13,14,],[14,14,14,]),'TYPE':([9,13,14,31,41,43,45,68,],[15,15,15,36,46,47,46,115,]),'D':([9,13,14,],[16,16,16,]),'G':([9,13,14,31,41,43,45,68,],[17,17,17,17,17,17,17,17,]),'C':([25,33,],[28,37,]),'E':([31,],[34,]),'formals':([31,],[35,]),'block':([38,44,49,138,140,155,],[40,60,60,60,60,60,]),'F':([39,80,],[42,119,]),'H':([41,45,],[44,78,]),'vardecl':([41,45,],[45,45,]),'I':([44,49,],[48,82,]),'stmt':([44,49,138,140,155,],[49,49,149,150,156,]),'M':([44,49,138,140,155,],[50,50,50,50,50,]),'assign':([44,49,138,140,155,],[51,51,51,51,51,]),'call':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[52,52,88,88,88,88,88,88,88,88,88,88,88,88,52,52,88,52,]),'expr':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[56,56,86,91,116,121,123,126,127,128,131,137,142,145,56,56,142,56,]),'location':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[61,61,87,87,87,87,87,87,87,87,87,87,87,87,61,61,87,61,]),'method':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[62,62,89,89,89,89,89,89,89,89,89,89,89,89,62,62,89,62,]),'Pprima':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'P':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'T':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'unary':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'literal':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'V':([44,49,53,55,69,90,92,94,109,112,113,118,131,133,138,140,142,155,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'N':([53,],[85,]),'binary':([56,86,91,116,121,123,126,127,128,131,137,142,145,],[94,94,94,94,94,94,94,94,94,94,94,94,94,]),'U':([56,86,91,116,121,123,126,127,128,131,137,142,145,],[95,95,95,95,95,95,95,95,95,95,95,95,95,]),'J':([79,148,],[117,153,]),'Q':([113,],[129,]),'actuals':([113,],[130,]),'L':([117,135,],[134,147,]),'K':([117,135,],[135,135,]),'S':([131,142,],[143,151,]),'O':([149,],[154,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> programprim','program',1,'p_program','ansintactico.py',12),
  ('programprim -> classdecl programprim','programprim',2,'p_programp','ansintactico.py',16),
  ('programprim -> <empty>','programprim',0,'p_programp','ansintactico.py',17),
  ('classdecl -> CLASS ID A LLAVEIZQ B LLAVEDER','classdecl',6,'p_classdecl','ansintactico.py',23),
  ('A -> EXTENDS ID','A',2,'p_herencia','ansintactico.py',27),
  ('A -> <empty>','A',0,'p_herencia','ansintactico.py',28),
  ('B -> fielddecl B','B',2,'p_contprograma','ansintactico.py',33),
  ('B -> methdecl B','B',2,'p_contprograma','ansintactico.py',34),
  ('B -> <empty>','B',0,'p_contprograma','ansintactico.py',35),
  ('fielddecl -> TYPE ID C FINALIZADOR','fielddecl',4,'p_field','ansintactico.py',40),
  ('C -> COMA ID C','C',3,'p_declaracionopcional','ansintactico.py',44),
  ('C -> <empty>','C',0,'p_declaracionopcional','ansintactico.py',45),
  ('methdecl -> D ID PARENTIZQ E PARENTDER block','methdecl',6,'p_methdecl','ansintactico.py',50),
  ('D -> TYPE','D',1,'p_pdecltipo','ansintactico.py',54),
  ('D -> VOID','D',1,'p_pdecltipo','ansintactico.py',55),
  ('E -> formals','E',1,'p_declcontent','ansintactico.py',59),
  ('E -> <empty>','E',0,'p_declcontent','ansintactico.py',60),
  ('formals -> TYPE ID F','formals',3,'p_formals','ansintactico.py',65),
  ('F -> COMA TYPE ID F','F',4,'p_formalscontent','ansintactico.py',69),
  ('F -> <empty>','F',0,'p_formalscontent','ansintactico.py',70),
  ('TYPE -> G','TYPE',1,'p_typespecs','ansintactico.py',75),
  ('G -> INT','G',1,'p_typespecint','ansintactico.py',79),
  ('G -> BOOLEAN','G',1,'p_typespecint','ansintactico.py',80),
  ('G -> STRING','G',1,'p_typespecint','ansintactico.py',81),
  ('G -> ID','G',1,'p_typespecint','ansintactico.py',82),
  ('G -> TYPE CORCHIZQ CORCHDER','G',3,'p_typespecint','ansintactico.py',83),
  ('block -> LLAVEIZQ H I LLAVEDER','block',4,'p_block','ansintactico.py',88),
  ('H -> vardecl H','H',2,'p_vardeclH','ansintactico.py',92),
  ('H -> <empty>','H',0,'p_vardeclH','ansintactico.py',93),
  ('I -> stmt I','I',2,'p_stmtI','ansintactico.py',98),
  ('I -> <empty>','I',0,'p_stmtI','ansintactico.py',99),
  ('vardecl -> TYPE ID J L FINALIZADOR','vardecl',5,'p_vardecl','ansintactico.py',104),
  ('J -> ASIGNAR expr','J',2,'p_vardeclJ','ansintactico.py',108),
  ('J -> <empty>','J',0,'p_vardeclJ','ansintactico.py',109),
  ('K -> COMA ID J','K',3,'p_vardeclk','ansintactico.py',114),
  ('L -> K L','L',2,'p_vardecll','ansintactico.py',118),
  ('L -> <empty>','L',0,'p_vardecll','ansintactico.py',119),
  ('stmt -> M','stmt',1,'p_stmt','ansintactico.py',124),
  ('M -> assign FINALIZADOR','M',2,'p_stmtmas','ansintactico.py',128),
  ('M -> call FINALIZADOR','M',2,'p_stmtmas','ansintactico.py',129),
  ('M -> RETURN N','M',2,'p_stmtmas','ansintactico.py',130),
  ('M -> IF PARENTIZQ expr PARENTDER stmt O','M',6,'p_stmtmas','ansintactico.py',131),
  ('M -> WHILE PARENTIZQ expr PARENTDER stmt','M',5,'p_stmtmas','ansintactico.py',132),
  ('M -> BREAK FINALIZADOR','M',2,'p_stmtmas','ansintactico.py',133),
  ('M -> CONTINUE FINALIZADOR','M',2,'p_stmtmas','ansintactico.py',134),
  ('M -> block','M',1,'p_stmtmas','ansintactico.py',135),
  ('N -> expr','N',1,'p_stmtmreturnn','ansintactico.py',140),
  ('N -> <empty>','N',0,'p_stmtmreturnn','ansintactico.py',141),
  ('O -> ELSE stmt','O',2,'p_stmtmifo','ansintactico.py',146),
  ('O -> <empty>','O',0,'p_stmtmifo','ansintactico.py',147),
  ('assign -> location ASIGNAR expr','assign',3,'p_assign','ansintactico.py',152),
  ('location -> method','location',1,'p_locationPprima','ansintactico.py',156),
  ('location -> Pprima','location',1,'p_locationPPrima','ansintactico.py',160),
  ('method -> P','method',1,'p_method','ansintactico.py',164),
  ('P -> ID','P',1,'p_locationpid','ansintactico.py',168),
  ('P -> expr ACCESO ID','P',3,'p_locationpid','ansintactico.py',169),
  ('Pprima -> expr CORCHIZQ expr CORCHDER','Pprima',4,'p_locationpexprexpr','ansintactico.py',174),
  ('call -> method PARENTIZQ Q PARENTDER','call',4,'p_call','ansintactico.py',178),
  ('Q -> actuals','Q',1,'p_callQ','ansintactico.py',182),
  ('Q -> <empty>','Q',0,'p_callQ','ansintactico.py',183),
  ('actuals -> expr S','actuals',2,'p_actuals','ansintactico.py',188),
  ('S -> expr S','S',2,'p_actualsS','ansintactico.py',192),
  ('S -> <empty>','S',0,'p_actualsS','ansintactico.py',193),
  ('expr -> T','expr',1,'p_expr','ansintactico.py',199),
  ('T -> location','T',1,'p_Tlocation','ansintactico.py',203),
  ('T -> call','T',1,'p_Tlocation','ansintactico.py',204),
  ('T -> THIS','T',1,'p_Tlocation','ansintactico.py',205),
  ('T -> NEW ID PARENTIZQ PARENTDER','T',4,'p_Tlocation','ansintactico.py',206),
  ('T -> NEW TYPE CORCHIZQ expr CORCHDER','T',5,'p_Tlocation','ansintactico.py',207),
  ('T -> expr ACCESO LENGTH','T',3,'p_Tlocation','ansintactico.py',208),
  ('T -> expr binary expr','T',3,'p_Tlocation','ansintactico.py',209),
  ('T -> unary expr','T',2,'p_Tlocation','ansintactico.py',210),
  ('T -> literal','T',1,'p_Tlocation','ansintactico.py',211),
  ('T -> PARENTIZQ expr PARENTDER','T',3,'p_Tlocation','ansintactico.py',212),
  ('binary -> U','binary',1,'p_binary','ansintactico.py',218),
  ('U -> MODULO','U',1,'p_Uresiduo','ansintactico.py',222),
  ('U -> YAND','U',1,'p_Uresiduo','ansintactico.py',223),
  ('U -> OOR','U',1,'p_Uresiduo','ansintactico.py',224),
  ('U -> MENORQUE','U',1,'p_Uresiduo','ansintactico.py',225),
  ('U -> MENORIGUAL','U',1,'p_Uresiduo','ansintactico.py',226),
  ('U -> MAYORQUE','U',1,'p_Uresiduo','ansintactico.py',227),
  ('U -> MAYORIGUAL','U',1,'p_Uresiduo','ansintactico.py',228),
  ('U -> COMPIGUAL','U',1,'p_Uresiduo','ansintactico.py',229),
  ('U -> COMPDIFERENTE','U',1,'p_Uresiduo','ansintactico.py',230),
  ('U -> PLUS','U',1,'p_Uresiduo','ansintactico.py',231),
  ('U -> MINUS','U',1,'p_Uresiduo','ansintactico.py',232),
  ('U -> POR','U',1,'p_Uresiduo','ansintactico.py',233),
  ('U -> DIVIDE','U',1,'p_Uresiduo','ansintactico.py',234),
  ('unary -> NEGLOGICA','unary',1,'p_unarydiferente','ansintactico.py',239),
  ('literal -> V','literal',1,'p_literal','ansintactico.py',243),
  ('V -> NUMERO','V',1,'p_V','ansintactico.py',247),
  ('V -> CADENA','V',1,'p_V','ansintactico.py',248),
  ('V -> TRUE','V',1,'p_V','ansintactico.py',249),
  ('V -> FALSE','V',1,'p_V','ansintactico.py',250),
  ('V -> NULL','V',1,'p_V','ansintactico.py',251),
]
