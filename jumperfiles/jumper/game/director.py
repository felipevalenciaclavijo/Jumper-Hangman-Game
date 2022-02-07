from game.terminal_service import TerminalService
from game.guesser import Guesser
from game.word_generator import Word_generator
from game.parachute import Parachute


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        guesser: The game's player/guesser.
        is_playing (boolean): Whether or not to keep playing.
        word generator: Generates a random word and splits it into letters.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._word_generator = Word_generator()
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        self._parachute = Parachute()
        self._word_line = []
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_line()
        self._terminal_service.write_text(self._parachute.get_parachute)
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Accepts a new guess from the user.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._terminal_service.read_text("\nGuess a letter [a-z]:  ")
        self._guesser.collect_guesses(self, guess)

    def play_again(self):


        playing_answer = self._terminal_service.read_text("\nWould you like to play again? [y/n]: ")
        if playing_answer.lower() == "y":
            self._is_playing() == True
        else:
            self._terminal_service.write_text("Thanks for playing!")
        
    def _do_updates(self):
        """Updates the parachute and the word line following guesses.

        Args:
            self (Director): An instance of Director.
        """
        if self._guesser.get_guesses()[-1] not in self._word_generator.get_generated_word():
            self.__parachute.cut_string()
        
    def _do_outputs(self):
        """Prints an instance of the Parachute.

        Args:
            self (Director): An instance of Director.
        """

        self._word_line()

        self._terminal_service.write_text(self._parachute.get_parachute)

    def _word_line(self):
        self._word_line = [x if x not in self._word_generator.get_generated_word() else "_" for x in self._guesser.get_guesses()]

        for i in self._word_line:
            print(i, end= " ")