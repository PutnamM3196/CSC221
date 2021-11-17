# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:50:47 2021

@author: putnamm3196
"""

import random as rand
def tournament():
    #randTime = rand.randint(5, 10)
    randomizer1 = 1
    randomizer2 = 1
    count = 0
    playerCorrect = 0
    computerCorrect = 0
    chkloop = True
    print("You will be playing with a computer player.")
    for i in range(5):
        chkloop = True
        randomizer1 += rand.randint(1, 20)
        randomizer2 += rand.randint(1, 20)
        num1 = rand.randint(5, randomizer1)
        num2 = rand.randint(5, randomizer2)
        userInt = 0
        print(num1,"+",num2,"=")
        ans = num1 + num2
        while chkloop == True:
            userInt = int(input("What's the answer?\n> "))
        
            if userInt == ans:
                print("Correct!")
                playerCorrect += 1
                chkloop = False
            elif userInt != ans: 
                print("Wrong")
                count += 1
                if count == 2:
                    print("Passing on to Computer")
                    chkloop = False
            
    
        randans1 = ans + 3
        randans2 = ans - 3
        compGuess = rand.randint(randans2, randans1)
        print(compGuess)
        if ans == compGuess:
            print("Computer got it correct")
            computerCorrect += 1
        else:
            print("Computer got the answer wrong\nPassing to you now.")
        print("\nPlayer Score:",playerCorrect)
        print("Computer Score",computerCorrect,"\n")
    if playerCorrect < computerCorrect:
        print("Computer Won")
    else:
        print("You won!")
        


tournament()
