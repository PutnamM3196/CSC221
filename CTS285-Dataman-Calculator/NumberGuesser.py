import random



def numGuess():
    loop = True
    count = 1
    num = random.randint(9, 100)
    
    lowGuess = random.randint(1, 9)
    highGuess = random.randint(1, 9)
    lowGuess = num - lowGuess
    highGuess = num + highGuess
    
    while loop == True:
        try:
            print("The number is between", lowGuess, "and", highGuess)
            userNum = int(input("Enter your guess: "))
            
            
            if userNum < num:
                print("To Low")
                count += 1
            elif userNum > num:
                print("To High")
                count += 1
            elif userNum == num:
                count += 1
                print("Good job, you're correct!")
                print("It took you",count,"tries.")
                loop = False
            else:
                print("Error")
        except ValueError:
            print("Please enter a value")
            
