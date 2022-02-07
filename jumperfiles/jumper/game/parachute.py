
class Parachute:

    """The game board creator. 
    
    The responsibility of a Parachute is to generate the game board based on user input
    and the generated word.
    
    Attributes:
        strings cut: the number of incorrect guesses.
        parachute: an instance of the parachute game board
    """

    def __init__(self):
        """Constructs a new Parachute.
        
        Args:
            self (Director): an instance of Director.
        """
        self._strings_cut = 0
        self._parachute = ["   ___   ",
             "  /   \  ",
             "   ___   ",
             "  \   /  ",
             "   \ /   ",
             "    0    ",
             "    |    ",
             "   /|\   ",
             "   / \   ",
             "         ",
             "^^^^^^^^^"]
             
    def get_parachute(self):
        text = ""
        if self._strings_cut >= 5:
            text = text + "    X    \n"
            for line in self._parachute[6:]:
                text = text + (line + "\n")
        else:
            for line in self._parachute[self._strings_cut:]:
                text = text + (line + "\n")
        return text 

    def cut_string(self):
        self._strings_cut += 1