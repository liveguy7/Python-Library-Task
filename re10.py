import string

n = string.ascii_lowercase
print(n)

n = str(5)
print(n)
s = input("Enter value ")
if(s.isdigit()):
  print(int(s) * 3)
else:
  print(f'Cannot turn {s} into an integer')

y = string.digits
print(y)

o = input("Enter a number ")
if(o.isdigit()):
  print(int(s) * 3)
else:
  bad_characters = []
  for one_character in s:
    if(one_character not in string.digits):
      bad_characters.append(one_character)
  print(f'Cannot turn into an integer: {bad_characters}')




