a = "Hello Python!"

IndexList = range(0, 13)

for index in IndexList:
    r = a[index]
    print(r)
print('# ------------------------------------ #')
b = "Hello Python!"

IndexList = range(0, len(b))

for index in IndexList:
    r = b[index]
    print(r)
print('# ------------------------------------ #')
Names = ["John", "Jane", "Doe", "Alice", "Bob"]

IndexList = range(0, 4)

for index in IndexList:
    r = Names[index]
    print(r)
print('# ------------------------------------ #')
Names = ["John", "Jane", "Doe", "Alice", "Bob"]

IndexList = range(0, 4)

for index in IndexList:
    r = Names[index]
    print(F"{index}:{r}")
    print(str(index) + ":" + r)
    print(index, ":", r)
print('# ------------------------------------ #')
