class Nodo:
    pass

class Statement(Nodo):
    def __init__(self, ide, exp):
        self.ide=ide
        self.exp=exp
    def evaluar(self):
        return self.exp.evaluar()
        

class ExpOp(Nodo):
    def __init__(self, op1, op, op2):
        self.op1=op1
        self.op=op
        self.op2=op2
    def evaluar(self):
        if self.op=='+':
            self.valor= self.op1.evaluar()+self.op2.evaluar()
        elif self.op=='-':
            self.valor= self.op1.evaluar()-self.op2.evaluar()
        elif self.op=='*':
            self.valor= self.op1.evaluar()*self.op2.evaluar()
        elif self.op=='/':
            self.valor= self.op1.evaluar()/self.op2.evaluar()
            
        return self.valor
                    
        
class ExpGrupo(Nodo):
    def __init__(self, exp):
        self.exp=exp
        
    def evaluar(self):
        return self.exp.evaluar()

class ExpNumero(Nodo):
    def __init__(self, valor):
        self.valor=valor
    def evaluar(self):
        return self.valor
   
        
        
        
    
    
