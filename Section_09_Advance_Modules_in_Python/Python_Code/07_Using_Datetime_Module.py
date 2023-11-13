import datetime


a = datetime.datetime.now()
print(a)
print(a.year)
print(a.month)
print(a.day)
# --------------------------------------------------------

b = str(a.year) + "/" + str(a.month) + "/" + str(a.day)
print(b)
# --------------------------------------------------------

c = str(a.year) + "/" + str(a.day) + "/" + str(a.month)
print(c)
# --------------------------------------------------------

d = f"{a.year}/{a.month}/{a.day}"
print(d)
# --------------------------------------------------------

e = f"{a.year}-{a.month}-{a.day}"
print(e)
# --------------------------------------------------------

print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
# --------------------------------------------------------

f = f"{a.hour}:{a.minute}:{a.second}:{a.microsecond}"
print(f)
# --------------------------------------------------------

g = f"{a.hour}:{a.minute}"
print(g)
# --------------------------------------------------------

h = f"{a.hour}:{a.minute}:{a.second}"
print(h)
# --------------------------------------------------------
