


import random

def memBank():
    storage = [1,2,3,4,5,6,7,8,9]
    
    num1 = random.choice(storage)
    num2 = random.choice(storage)
    operator = int(input("""
What operation do we want to practice with? 
1. Addition
2. Subtraction
3. Multiplication

"""))
    if operator == 1:
        ans = num1 + num2
        sign = "+"
    elif operator == 2:
        ans = num1 - num2
        sign = "-"
    elif operator == 3:
        ans = num1 * num2
        sign = "*"
    
    print(num1, sign, num2," = ")
    userInput = int(input("What's the answer? \n>"))
    if userInput == ans:
        print("You're correct!")
        ask = int(input("Do you want to continue?\n\
1. Yes\n\
2. No\n"))
        if ask ==  1:
            memBank()
        elif ask == 2:
            return
        else:
                print("Error")
    elif userInput != ans:
        print("Wrong.")
    else:
        print("Error")
