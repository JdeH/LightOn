class Dog:                      # Define the dog species
    def __init__ (self, sound): # Constructor, named __init__, accepts provided sound
        self.sound = sound      # Stores accepted sound into self.sound field inside new dog

    def bark (self):            # Define bark method
        print (self.sound)      # Prints the self.sound field stored inside this dog
        
your_dog = Dog ('Wraff')        # Instantiate dog, provide sound "Wraff" to constructor
neighbours_dog = Dog ('Wooff')  # Instantiate dog, provide sound "Wooff" to constructor

your_dog.bark ()                # Prints "Wraff"
neighbours_dog.bark ()          # Prints "Wooff"
