CurrentTry = 1
TotalGuesses = 3
CorrecyAnswer = "Horse"
FirstLetter = CorrecyAnswer[0]

while CurrentTry <= 3:
    UserAnswer = input(f"Guress the animal name starting with '{FirstLetter}': ")

    UserAnswer = UserAnswer.replace(" ", "")

    if UserAnswer == "":
        print("Enter the valid animal name!")

    if UserAnswer == CorrecyAnswer:
        print("You Win!")
        break
    else:
        print("")
        print(f"Wrong Answer! Try Again! Left({TotalGuesses - CurrentTry} of {TotalGuesses})")

    CurrentTry += 1

else:
    print("You Lost!")
