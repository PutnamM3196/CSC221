


import random as rand
def missNum():
    loop = True
    num1 = rand.randint(0, 10)
    num2 = rand.randint(0, 10)
    userInput = int(input("""
What operation do we want to practice with? 
1. Addition
2. Subtraction
3. Multiplication

"""))
    while loop == True:
        if userInput == 1:
            ans = num1 + num2
            print("[ ] +", num2,"=",ans)
            userAns = int(input("What number goes into the box?\n"))
            if userAns == num1:
                print("Correct!")
                loop = False
            elif userAns != num1:
                print("Wrong. Try Again.")
        elif userInput == 2:
            ans = num1 - num2
            print("[ ] -", num2,"=",ans)
            userAns = int(input("What number goes into the box?\n"))
            if userAns == num1:
                print("Correct!")
                loop = False
            elif userAns != num1:
                print("Wrong. Try Again.")
        elif userInput == 3:
            ans = num1 * num2
            print("[ ] *", num2,"=",ans)
            userAns = int(input("What number goes into the box?\n"))
            if userAns == num1:
                print("Correct!")
                loop = False
            elif userAns != num1:
                print("Wrong. Try Again.")
        else:
            print("Error")