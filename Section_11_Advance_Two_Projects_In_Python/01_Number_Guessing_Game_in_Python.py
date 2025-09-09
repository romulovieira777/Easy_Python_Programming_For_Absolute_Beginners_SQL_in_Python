CurrentTry = 1
TotalGuesses = 3
CorrecyAnswer = 6

while CurrentTry <= 3:
    UserAnswer = input("Enter a number between 0 to 9: ")

    UserAnswer = UserAnswer.replace(" ", "")

    if UserAnswer == "":
        print("Enter the valid number!")
        continue

    UserAnswer = int(UserAnswer)

    if UserAnswer == CorrecyAnswer:
        print("You Win!")
        break
    else:
        print("")
        print(f"Wrong Answer! Try Again! Left({TotalGuesses - CurrentTry} of {TotalGuesses})")

    CurrentTry += 1

else:
    print("You Lost!")
