# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:42:53 2021

@author: putnamm3196
"""

from Item import Item

class Container:
    """ This class only handles collections of Items. """
    
    def __init__(self):
        self.contents = {}
        
    def add(self, item):
        self.contents[item.name] = item
        
    def remove(self, item):
        if self.contains(item.name):
            # remove the item from the dictionary
            del self.contents[item.name]

    def moveItemTo(self, item, destination):
        
        destination.add(item)
        self.remove(item)
        
    def listContents(self):
        text = ""
        for key in self.contents:
            text += key 
            text += " : " 
            text += self.contents[key].description
            text += "\n"
        return text
           
    def contains(self, itemName):
        """ quick way to check if item is present. """
        # keys() gives us a list of names of items present
        itemNameList = list(self.contents.keys())
        #print(itemNameList)
        if itemName in itemNameList:
            return True
        else:
            return False

 
        
def main():
     """ test code"""
     
     
 
    
 
if __name__ == "__main__":
    main()