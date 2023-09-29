dof = input("Enter the Date of Birth (yyyy/mm/dd): ")
year = int(dof[0:4])
Age = 2023 - year

print("Your Date of Birth is:", dof)
print("Your Year of Birth is:", year)
print("Your Age is:", Age, "Years Old!")
# -------------------------------------------------------
dof = input("Enter the Date of Birth (dd/mm/yyyy): ")
year = int(dof[-4:])
Age = 2023 - year

print("Your Date of Birth is:", dof)
print("Your Year of Birth is:", year)
print("Your Age is:", Age, "Years Old!")
