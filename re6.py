import re

s = 'abdefgabcdefgabcdefgx'
n = s.replace('e,', 'X')
print(n)
n = re.sub('[ae]', 'X', s)
print(n)
n = re.subn('[ae]', 'X', s, 200)
print(n)


def star_vowel(m):
  return f'*{m.group(0)}*'


n = re.sub('[ae]', star_vowel, s, 2)
print(n)


def star_ord(m):
  return f'*{ord(m.group(0))}*'


n = re.sub('[ae]', star_ord, s, 2)
print(n)
