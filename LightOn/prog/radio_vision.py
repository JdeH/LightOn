class Radio:
    def __init__ (self, sound):
        self.sound = sound
        
    def play (self):
        print ('Saying:', self.sound)
        print ()

class Television (Radio):
    def __init__ (self, sound, picture):
        Radio.__init__ (self, sound)
        self.picture = picture
        
    def play (self):
        self._show ()
        Radio.play (self)
        
    def _show (self):
        print ('Showing:', self.picture)
        
tuner = Radio ('Good evening, dear listeners')
carradio = Radio ('Doowopadoodoo doowopadoodoo')
television = Television ('Here is the latest news', 'Newsreader')

print ('TUNER')
tuner.play ()

print ('CARRRADIO')
carradio.play ()

print ('TELEVISION')
television.play ()