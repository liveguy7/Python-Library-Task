import re

s = 'Hello?? Is anyone there?'

n = re.findall(re.escape(r'Jello??'), s)

print(n)


