
# parsetab.py
# This file is automatically generated. Do not edit.

_lr_method = 'LALR'

_lr_signature = '\xe4y-D\x0e?\x9e4v\xa3\xb3\x1c=\xe0\xc1\xd0'

_lr_action_items = {'DIVISION':([1,2,5,7,8,13,14,15,16,17,18,],[-9,-8,9,-9,9,9,-7,-6,9,9,-5,]),'MAS':([1,2,5,7,8,13,14,15,16,17,18,],[-9,-8,10,-9,10,10,-7,-6,-3,-4,-5,]),'IDENT':([0,3,6,9,10,11,12,],[1,7,7,7,7,7,7,]),'PARENDER':([2,7,8,14,15,16,17,18,],[-8,-9,14,-7,-6,-3,-4,-5,]),'NUMERO':([0,3,6,9,10,11,12,],[2,2,2,2,2,2,2,]),'IGUAL':([1,],[6,]),'MENOS':([1,2,5,7,8,13,14,15,16,17,18,],[-9,-8,11,-9,11,11,-7,-6,-3,-4,-5,]),'MULT':([1,2,5,7,8,13,14,15,16,17,18,],[-9,-8,12,-9,12,12,-7,-6,12,12,-5,]),'PARENIZQ':([0,3,6,9,10,11,12,],[3,3,3,3,3,3,3,]),'$end':([1,2,4,5,7,13,14,15,16,17,18,],[-9,-8,0,-2,-9,-1,-7,-6,-3,-4,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,6,9,10,11,12,],[5,8,13,15,16,17,18,]),'statement':([0,],[4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('statement',3,'p_statement_assign','calcyacc.py',18),
  ('statement',1,'p_statement_expr','calcyacc.py',24),
  ('expression',3,'p_expression_binop','calcyacc.py',30),
  ('expression',3,'p_expression_binop','calcyacc.py',31),
  ('expression',3,'p_expression_binop','calcyacc.py',32),
  ('expression',3,'p_expression_binop','calcyacc.py',33),
  ('expression',3,'p_expression_group','calcyacc.py',39),
  ('expression',1,'p_expression_number','calcyacc.py',44),
  ('expression',1,'p_expression_name','calcyacc.py',50),
]