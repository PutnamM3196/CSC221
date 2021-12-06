# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:50:17 2021

@author: putnamm3196
"""


import Game
import random as rand
def main():
    loop = True
    playerHealth = 50
    enemyHealth = 50
    print("""
You begin to fight a goblin.
You get the jump on the goblin, what do you do?
""")
    while loop == True:
        user_action = int(input("""1. Stab 2. Swipe\n> """))
        if user_action == 1:
            chance = rand.randint(75, 100)
            if chance > 75:
                enemyHealth -= 20
                print("You hit for 20 damage")
                if enemyHealth <= 0:
                    print("You Win!\n You win 5 gold")
                    Game.money += 5
                    return
                    
            else:
                print("Miss")
        elif user_action == 2:
            chance = rand.randint(30, 100)
            if chance > 30:
                enemyHealth -= 10
                print("You hit for 10 damage")
                if enemyHealth <= 0:
                    print("You Win!\n You win 5 gold")
                    Game.money += 5                    
                    return
            else:
                print("Miss")
        else:
            print("Error")
            
        enemyHit = rand.randint(1, 2)
        if enemyHit == 1:
            chance = rand.randint(75, 100)
            if chance > 75:
                playerHealth -= 20
                print("Goblin hits for 20 damage")
                if playerHealth <= 0:
                    print("You Lose!")
                    return
            else:
                print("The goblin misses")
        elif enemyHit == 2:
            chance = rand.randint(30, 100)
            if chance > 50:
                playerHealth -= 10
                print("Goblin hits for 10 damage")
                if playerHealth <= 0:
                    print("You Lose!")
                    return
            else:
                print("The goblin misses")
if __name__ == "__main__":
    main()
                
