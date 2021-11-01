# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:21:09 2021

@author: putnamm3196
"""

from Game import Game
from Room import Room
from Player import Player
from Item import Item

class MyGame(Game):
    def setup(self):
        loader = MyGameLoader()
        self.rooms = loader.setup()
        self.here = self.rooms["Hub"]
        self.here.describe()
        
        
class MyGameLoader: 
    def setup(self):
        """ setup(): create a graph of rooms for play. """
        # just a test -- needs work

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
    
def main():
    game = MyGame()
    game.setup()
    game.output("""
Starting game -- type help if needed  -- enter command.
Welcome to the start of your journey! Your goal is to train your
character to defeat the epic dragon. To start, you should go to the weaponsmith
to get your sword.""")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()