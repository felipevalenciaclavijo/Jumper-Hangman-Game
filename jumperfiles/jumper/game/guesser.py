

class Guesser:
    """The person guessing the word. 
    
    The responsibility of Guesser is to keep track of past guesses. 
    
    Attributes:
        _guesses : a list of guesses
        
    """

    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesses): An instance of Guesser.
        """
        self._guesses = []


    def collect_guesses(self, guess):
        self._guesses.append(guess)
    

    def get_guesses(self):
        """Gets guesses.

        Args:
            self (Guesser): An instance of Guesser.
        
        Returns:
            the new appended list of guesses so far.
        """
    
        return self._guesses