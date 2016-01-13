import time

class HumanBeing:
    def __init__ (self, name):
        self.description = name + ' the ' + self.__class__.__name__.lower ()
       
    def walk (self):
        self._begin_walk ()
        for i in range (5):
            print (self.description, 'is counting', i + 1)
        self._end_walk ()
        print ()
        
class NatureLover (HumanBeing):
    def _begin_walk (self):
        print (self.description, 'goes to the park')
        
    def _end_walk (self):
        print (self.description, 'returns from the park')
        

class CouchPotato (HumanBeing):
    def _begin_walk (self):
        print (self.description, 'lets the dino escape')
        
    def _end_walk (self):
        print (self.description, 'catches the dino')
        
class OutdoorSleeper (NatureLover, CouchPotato):
    def _begin_walk (self):
        NatureLover._begin_walk (self)
        CouchPotato._begin_walk (self)
        print (self.description, 'lies on the park bench')
        
    def _end_walk (self):
        print (self.description, 'gets up from the park bench')
        CouchPotato._end_walk (self)
        NatureLover._end_walk (self)
        
for human_being in (NatureLover ('Wilma'), CouchPotato ('Fred'), OutdoorSleeper ('Barney')):
    human_being.walk ()