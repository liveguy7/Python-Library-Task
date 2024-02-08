import re

s = 'this is the programming language python'

n = re.search('python', s)
print(n)
print(n)
n = re.findall(r'\b[A-Z][a-z]+\b', s)
print(n)
m = re.search('asdfafa', s)
print(m.group(0))
