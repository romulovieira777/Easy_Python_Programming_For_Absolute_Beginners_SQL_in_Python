EmpName = "Mj"
EmpAge = 19

if EmpName == "Mj" and EmpAge >= 19:
    print("This is valid Employee!")
else:
    print("This is not valid Employee!")
# ----------------------------------------------
if EmpName == "Mj" or EmpAge >= 19:
    print("This is valid Employee!")
else:
    print("This is not valid Employee!")
# ----------------------------------------------
b = False

print(not b)
# ----------------------------------------------
if not (EmpName == "Mj" and EmpAge >= 19):
    print("This is valid Employee!")
else:
    print("This is not valid Employee!")
# ----------------------------------------------
