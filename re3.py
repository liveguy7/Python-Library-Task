import re

email = 'pan@na.com'
s = 'abcd\nefgh\nijkl\nmnop\n'
words = 'these are some words, these are some words'
print(words[:1000])
re.findall('^a.+z$', words)
re.findall('^a\w+e$', words, re.MULTILINE|re.IGNORECASE)
b = re.findall('^A\w+Z$', words, re.MULTILINE|re.IGNORECASE|re.VERBOSE)
print(b)
j = re.search('cD.Ef', s, re.S|re.I)
m = re.search('pan', email, re.I)

if j:
  print(j.group(0))
else:
  print('no match')

