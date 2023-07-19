# Notes from week 7 (Module 7)

# OOP

# Class example
class Player():
    min_health = 1000
    
    # dunder method
    def __init__(self, name, health, hunger):
        self.name = name
        self.health = health
        self.setHunger(hunger)
    
    # mutator example  
    def setHunger(self, hunger):
        self.hunger = hunger
        
# Class testing
me = Player("bob", "good", 10)
Player.min_health = 500
print(me.hunger)
print(me.min_health)