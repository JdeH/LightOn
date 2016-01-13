class Observer:
    def update (self):          # Only here to clarify the interface
        raise Exception ('Abstract method called: Observer.update')
                                # Google for 'Python' and 'exception'
class Subject:
    def __init__ (self):
        self.observers = []
        
    def attach (self, observer):
        self.observers.append (observer)    # Forward link to observers
        observer.subject = self # Backlink from observer to subject
        observer.update ()      # Get new observer up to date
        
    def detach (self, observer):
        self.observers.remove (observer)
        
    def notifyObservers (self):
        for observer in self.observers:
            observer.update ()

class TicTacToeObserver (Observer):
    def update (self):
        print ('\n'.join ([                 # Google for 'Python' and 'join'
            ' '.join ([                     # and also for 'nested list comprehensions'
                self.symbols [value]        # Use common sense and perseverance
                for value in row            # to discover what happens here
            ])                              # Write a small test program to
            for row in self.subject.state   # experiment with code like this
        ]), '\n')                           # Try the same without list comprehensions
        
class AlphaObserver (TicTacToeObserver):
    symbols = ('.', 'O', 'X')               # Inherited update will use these symbols

class BinObserver (TicTacToeObserver):
    symbols = ('.', '0', '1')               # Inherited update will use these symbols

class TicTacToeSubject (Subject):
    def __init__ (self):
        Subject.__init__ (self)
        
        self.state = [                      # Initialize with 0's
            [0 for column in range (3)]     # 0 means empty field, 1 means nought, 2 means cross
            for row in range (3)            # Nested list comprehensions again
        ]                                   # Try to reformulate without list comprehensions
        
    def play (self):
        even = False                        # The odd player starts, the even player is next
        while True:
            print ('X1' if even else 'O0', 'player' )
            rowKey = input ('Row (q = quit):')  # Variable rowKey will contain a string of characters
                                                # rather than an integer number, so e.g. '3' rather than 3 
            if rowKey == 'q':                   # You can't calculate with strings, only with numbers.
                break
                
            columnKey = input ('Column:')
            self.state [int (rowKey) - 1][int (columnKey) - 1] = 2 if even else 1   # Convert to integers
            even = not even                 # It's the other player's turn now
            self.notifyObservers ()         # Let the views know something has changed
            
ticTacToeSubject = TicTacToeSubject ()      # Create the game

ticTacToeSubject.attach (AlphaObserver ())  # Attach the observers
ticTacToeSubject.attach (BinObserver ())

ticTacToeSubject.play ()                    # Start playing
