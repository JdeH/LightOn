class NatureLover:              # Define a type of human being that loves nature
    def walk (self, dog):       # The NatureLover walks the dog, really
        print ('\nC\'mon!')     # \n means start on new line, \' means ' inside string
        dog.follow_me ()        # Just lets it escape

class CouchPotato:              # Define a type of human being that loves couchhanging
    def walk (self, dog):       # The CouchPotato walks the dog, well, lets it go
        print ('\nBugger off!') # \n means start on new line
        dog.escape ()           # Just lets it escape

class Dog:                      # Define the dog species
    def __init__ (self, sound): # Constructor, named __init__, accepts provided sound
        self.sound = sound      # Stores accepted sound into self.sound field inside new dog

    def _bark (self):           # Define _bark method, not part of interface of dog
        print (self.sound)      # It prints the self.sound field stored inside this dog
        
    def follow_me (self):       # Define escape method
        print ('Walk behind')   # The dog walks one step behind the boss
        self._bark ()           # It then calls upon its own _bark method
        self._bark ()           # And yet again
        
    def escape (self):          # Define escape method
        print ('Hang head')     # The dog hangs his head
        self._bark ()           # It then calls upon its own _bark method
        self._bark ()           # And yet again
        
your_dog = Dog ('Wraff')        # Instantiate dog, provide sound "Wraff" to constructor
his_dog = Dog ('Howl')          # Instantiate dog, provide sound "Howl" to constructor
        
you = NatureLover ()            # Create yourself
your_friend = CouchPotato ()    # Create your friend

you.walk (your_dog)             # Interface: walk dog, implementation: going out together
your_friend.walk (his_dog)      # Interface: walk dog, implementation: sending dog out