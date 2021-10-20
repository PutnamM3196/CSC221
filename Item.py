#Item Class

class Item:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return self.name + " : " + self.description




def main():
    key = Item("key", "A rusty key")
    
    sword = Item("sword", "rusty sword")
    
    stuff = [key, sword]
    for item in stuff:
        print(item)
        
if __name__ == "__main__":
    main()