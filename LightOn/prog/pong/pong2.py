class Paddle:
    def __init__ (self, game, index):
        self.game = game    # A paddle knows which game object it's part of
        self.index = index  # A paddle knows its index, 0 (left) or 1 (right)
                
class Ball:
    def __init__ (self, game):
        self.game = game    # A ball knows which game object it's part of

class Scoreboard:
    def __init__ (self, game):
        self.game = game    # A scoreboard knows which game object it's part of
 
class Game:
    def __init__ (self):
        self.paddles = [Paddle (self, index) for index in range (2)]    # Pass game as parameter self
        self.ball = Ball (self)
        self.scoreboard = Scoreboard (self)
                
game = Game ()  # Create game, which will in turn create its paddles, ball and scoreboard
