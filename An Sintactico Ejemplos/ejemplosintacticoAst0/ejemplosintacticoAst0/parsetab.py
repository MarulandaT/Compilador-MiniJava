
# parsetab.py
# This file is automatically generated. Do not edit.

_lr_method = 'LALR'

_lr_signature = '\xc5\xad\xb5\xd6=|\xe7\xae&iJ\xf3r\xbfW3'

_lr_action_items = {'DIVISION':([1,2,8,9,10,11,12,13,],[-6,4,4,-4,4,4,-3,-5,]),'MAS':([1,2,8,9,10,11,12,13,],[-6,5,5,-4,-1,-2,-3,-5,]),'PARENDER':([1,8,9,10,11,12,13,],[-6,13,-4,-1,-2,-3,-5,]),'NUMERO':([0,3,4,5,6,7,],[1,1,1,1,1,1,]),'MENOS':([1,2,8,9,10,11,12,13,],[-6,6,6,-4,-1,-2,-3,-5,]),'MULT':([1,2,8,9,10,11,12,13,],[-6,7,7,-4,7,7,-3,-5,]),'PARENIZQ':([0,3,4,5,6,7,],[3,3,3,3,3,3,]),'$end':([1,2,9,10,11,12,13,],[-6,0,-4,-1,-2,-3,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,7,],[2,8,9,10,11,12,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('expression',3,'p_expression_binop','calcyacc.py',14),
  ('expression',3,'p_expression_binop','calcyacc.py',15),
  ('expression',3,'p_expression_binop','calcyacc.py',16),
  ('expression',3,'p_expression_binop','calcyacc.py',17),
  ('expression',3,'p_expression_group','calcyacc.py',21),
  ('expression',1,'p_expression_number','calcyacc.py',25),
]