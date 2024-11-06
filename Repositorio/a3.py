a = 222

b = a

b += 2
print(id(a), id(b))
print(a is b)