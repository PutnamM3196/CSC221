# CSC 221
# Text Adventure
# norrisa
# 10/1/21
from Container import Container
from Item import Item

class Room(Container):
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    """
        
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.contents = {}
    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        # append all exits
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        # print items in room, if any
        text += "In this room you see: \n"
        text += self.listContents()
        return text

 #   def __repr__(self):  # we're not using this yet
 #       pass


    def describe(self):
        """ print full room description. """
        print(self)
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.             
            
    def addItem(self, item):
        self.add(item)
    def removeItem(self, item):
        self.remove(item)
            



def main():
    """
    Currently used for testing.
    TODO: implement doctests. """
    dungeonEntrance = Room( "Dungeon Entrance", 
                   "",
                   { "east": "Hub",
                    "north": "Lobby"} )
    dungeonLobby = Room( "Lobby",
                        "",
                        {"south": "Dungeon Entrance",
                         "down": "Basement"})
    
    dungeonBasement = Room ( "Basement",
                      "",
                      {"up": "Lobby"})
    tournament = Room ( "Tournament",
                       "",
                       { "north" : "Hub"} )
    
    weaponShop = Room ( "Weapon Shop", 
                     "",
                     { "south" : "Hub" } )
    
    
    bossArena = Room ( "Boss Arena",
                   "",
                   {"west" : "Hub"})
    hub = Room ( "Hub",
                " ",
                {"north" : "Weapon Shop",
                 "south" : "Tournament",
                 "east" : "Boss Arena",
                 "west": "Dungeon Entrance"})
    
    # Place rooms in a dictionary.

    rooms = {dungeonEntrance.name: dungeonEntrance,
                dungeonLobby.name: dungeonLobby,
                dungeonBasement.name: dungeonBasement,
                tournament.name: tournament,
                weaponShop.name: weaponShop,
                bossArena.name: bossArena,
                hub.name: hub}
    phone = Item("phone","a mysterious device, probably should be thrown away.")
    hub.addItem(phone)
    
    sword = Item("sword","the best sword from the local blacksmith")
    weaponShop.addItem(sword)
    return rooms

 
    
    


if __name__ == "__main__":
    main()
