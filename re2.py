import re

s = 'what a wonerful day we are having'

try:
  print(re.findall('[a-t] {4}', s))
except re.error as e:
  print(f'regexp error: {e}')
  print(f'problem pattern: {e.pattern}')
  print(f'problem pos: {e.pos}')
  print(f'problem lineno: {e.lineno}')
  print(f'problem colno: {e.colno}')


print(type(re.error))
