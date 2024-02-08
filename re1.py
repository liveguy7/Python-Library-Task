import re

s = 'My SSN is 123-45-6997.'

m = re.search('(?P<first>\d{3})-(?P<second>\d{2})-(?P<third>\d{4})', s)

if m:
  print(m.groupdict())
  print(m.string)
  print(s[10:21])
  print(m.lastindex)
  print(len(s))
  print(m.group(0))
  print(m.group(1))
else:
  print('no match')