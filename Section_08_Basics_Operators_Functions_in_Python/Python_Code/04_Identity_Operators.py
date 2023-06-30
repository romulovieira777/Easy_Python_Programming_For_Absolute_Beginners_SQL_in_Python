a = "Hello Python!"
b = "Hi Python!"
r = a is b
print(r)
print(type(r))
# -----------------------

b = a is not b
print(b)
print(type(b))
# -----------------------

c = 13
d = 12
r = c is d
print(r)
print(type(r))
# -----------------------

r = c is not d
print(r)
print(type(r))
# -----------------------

x = " Hi love you!"
xx = " Hi love you!"
r = x is xx
print(r)
print(type(r))
# -----------------------
