class Attribute:    # Attribute in the gaming sense of the word, rather than of an object
    def __init__ (self, game):
        self.game = game                    # Done in a central place now
        self.game.attributes.append (self)  # Insert each attribute into a list held by the game
		
	# ============ Standard interface starts here
		
    def reset (self):
        pass    
        
    def predict (self):
        pass
                
    def interact (self):
        pass
        
    def commit (self):
        pass
		
	# ============ Standard interface ends here
 
class Sprite (Attribute):   # Here, a sprite is an rectangularly shaped attribute that can move
    def __init__ (self, game, width, height):
        self.width = width
        self.height = height
        Attribute.__init__ (self, game)     # Call parent constructor to set game attribute
        
class Paddle (Sprite):
    width = 10      # Constants are defined per class, rather than per individual object
    height = 100    # since they are the same for all objects of that class
                    # They are defined BEFORE the __init__, not INSIDE it
    def __init__ (self, game, index):
        self.index = index  # Paddle knows its player index, 0 == left, 1 == right
        Sprite.__init__ (self, game, self.width, self.height)
        
class Ball (Sprite):
    side = 8
    
    def __init__ (self, game):
        Sprite.__init__ (self, game, self.side, self.side)

class Scoreboard (Attribute):   # The scoreboard doesn't move, so it's an attribute but not a sprite
    pass
 
class Game:
    def __init__ (self):
        self.attributes = []    # All attributes will insert themselves into this polymorphic list
        
        self.paddles = [Paddle (self, index) for index in range (2)]
        self.ball = Ball (self)
        self.scoreboard = Scoreboard (self)
        
        for attribute in self.attributes:
            attribute.reset ()
        
    def update (self):                      #   To be called cyclically by game engine 
        for attribute in self.attributes:   #   Compute predicted values
            attribute.predict ()
            
        for attribute in self.attributes:   #   Correct values for bouncing and scoring
            attribute.interact ()
            
        for attribute in self.attributes:   #   Commit them to game engine for display
            attribute.commit ()
    
game = Game ()  # Create and run game
