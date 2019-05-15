import re
print re.match('[a-zA-Z_]\w+@[a-zA-Z]+\.[a-z]{2,3}(\.[a-z]{2})?$' , 'mm_832@gmail.com.co')

x =  re.match("http://.+\net",
              """http://mundogeek.net
et""")


print x
