from string import Template

t = Template('Welcome, $name, The price is $price')

print(t)
n = t.substitute(name='Reuven', price=100)
print(n)
a = t.safe_substitute(name='Reuven', price=90)
print(a)
t = Template('welcome, $name; the price is $price')
t.substitute(name=1, price=2)
print(t)
d = {'name': 'reuven', 'price': 100}
t.substitute(d)
print(t)

class MyTemplate(Template):
  delimiter = '!'

t = MyTemplate('welcome, !name. the price is !price')
t.substitute(name=1, price=2)
print(t)















