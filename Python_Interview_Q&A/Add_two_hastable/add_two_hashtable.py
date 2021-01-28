first = {"a":1,"b":2}
second={"c":3,"d":4}

third = first
third.update(second)
print(first)
print(second)
print(third)
print(id(third))
print(id(first))

#--------------------------------


a = {"a":1,"b":2}
b={"c":3,"d":4}

c = a.copy()
c.update(b)
print(a)
print(b)
print(c)
print(id(a))
print(id(c))