a = "Hello Python!"

for x in a:
    if x == "!":
        continue
    print(x)
else:
    print("Done!")
# ------------------------------------------------
Mylist = ["Python", "Java", "C++", "C#"]

for FirstName in Mylist:
    print(FirstName)
    if FirstName == "C++":
        continue
else:
    print("Done!")
# ------------------------------------------------
Mylist = ["Python", "Java", "C++", "C#"]

for x in Mylist:
    pass
