class HumanBeing:               # Define the human species
    def walk (self, dog):       # The human itself walks the dog
        print ('\nLets go!')    # \n means start on new line
        dog.escape ()           # Just lets it escape

class Dog:                      # Define the dog species
    def __init__ (self, sound): # Constructor, named __init__, accepts provided sound
        self.sound = sound      # Stores accepted sound into self.sound field inside new dog

    def bark (self):            # Define bark method
        print (self.sound)      # It prints the self.sound field stored inside this dog
        
    def escape (self):          # Define escape method
        print ('Run to tree')	# The dog will run to the nearest tree
        self.bark ()            # It then calls upon its own bark method
        self.bark ()            # And yet again
        
your_dog = Dog ('Wraff')        # Instantiate dog, provide sound "Wraff" to constructor
neighbours_dog = Dog ('Wooff')  # Instantiate dog, provide sound "Wooff" to constructor
        
you = HumanBeing ()             # Create yourself
mother = HumanBeing ()          # Create your mother

you.walk (your_dog)             # You walk your own dog
mother.walk (neighbours_dog)    # your mother walks the neighbours dog
