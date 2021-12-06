# CSC 221
# Text Adventure
# Mark Putnam
# 10/1/21

from Room import Room
from Player import Player
import Fight

class Game:

    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = { } 
        self.player = Player() 
        
        
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        
        

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def output(self, message):
        """ output the message. Just uses print() in base class.
        You might for example subclass to use Flask, etc. """
        print(message)

    def setup(self):
        """ setup(): create a graph of rooms for play. """
        

    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")
        


    def end(self):
        """ finish game, inform user of score and turns played. """
        pass
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)    
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        elif verb == "drop":
            item = words[1]
            self.commandDrop(item)
        elif verb == "use":
            item = words[1]
            if item == "sword":    
                self.commandFight(item)
            elif item == "phone":
                self.commandPhone(item)
            else:
                print("You can't fight with a",item)
        elif verb == "money":
            self.money(money)
        elif verb == "help":
            print("""
go [direction] -- Moves your character in that direction (ex. North)
look -- displays where you are
get [item] -- grabs the item
drop [item] -- drops the item
quit -- exits the game
""")
        
        else: # first word is verb
            print("I don't know how to", words[0])

    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            newRoomName = self.here.exits[direction]
            newRoom     = self.rooms[newRoomName]
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
    def money(self, money):
        print(self.here.money)
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """
        print("You try to get the", itemName)
        
        if self.here.contains(itemName):
            item = self.here.contents[itemName]
            self.here.moveItemTo(item, self.player)
            print("You pick up the",itemName)
        else:
            print("You can't see any", itemName, "here.")
    def commandFight(self, itemName):
        if self.player.contains(itemName):
            Fight.main()
        else:
            print("Don't have a sword")
    def commandPhone(self, itemName):
        if self.player.contains(itemName):
            print("Your phone has no signal")
    def commandDrop(self, itemName):
        """ remove the item from player inventory
        (if it's there) and add it to the room. 
        """
        print("You try to drop the", itemName)
        
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.player.moveItemTo(item, self.here)
            print("You drop the", itemName,".")
        else:
            print("You don't have a",itemName,".")
            

    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room

def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()