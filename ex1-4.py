import re

pat1 = re.compile('[0-9+]')

print("-----match-----")
m = re.match('[a-z]+', '01tem56po')
print(m)

print("-----saerch-----")
m = re.search('[a-z]+', '01tem56po')
print(m)
print(m.group())
print(m.span())
print(m.start())
print(m.end())

print("-----findall-----")
m = re.findall('[a-z]+', '01tem56po')
print(m)

print("-----findall-----")
m = re.findall('[a-zA-Z]+', 'This is a book.')
print(m)

print("-----findall-----")
m = re.findall('[a-z\'A-Z]+', "This isn't a book.")
print(m)

print("-----findall-----")
m = re.findall("[a-z'A-Z]+", "This isn't a book.")
print(m)
