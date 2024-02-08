import re

s = 'abc defhi,jklh fhg'
n = s.split(' ')
print(n)
n = s.split(',')
print(n)
n = re.split('[ ,]', s, 1)
print(n
     )