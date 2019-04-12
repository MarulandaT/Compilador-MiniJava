import re
#print re.match('[a-zA-Z_]\w+@[a-zA-Z]+\.[a-z]{2,3}(\.[a-z]{2})?$' , 'correo@gmail.com')

print re.match("http://.+\net",
              """http://mundogeek.net
et""")


