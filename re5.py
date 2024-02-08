import re

words = 'these are some mome words, these are ean some words'

ro = re.findall('a.*e.*p.*m', words)

for one_line in words:
  m = ro.search(one_line)
  if m:
    print(one_line, end='')

