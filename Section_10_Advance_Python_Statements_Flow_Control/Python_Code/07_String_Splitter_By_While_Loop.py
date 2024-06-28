x = "Hello Python!"
print(len(x))

l = len(x)
index = 0

while index < l:
    a = x[index]
    print(a)
    index += 1
else:
    print(f"It's done! Number of letters is {l}")
