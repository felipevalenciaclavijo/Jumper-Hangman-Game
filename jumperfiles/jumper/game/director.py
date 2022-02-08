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
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
               
        self._terminal_service.write_text('Welcome to Jumper! Guess the word before all parachute lines are cut.')

        # self._word_line(self._word_generator.get_split_generated_word(), self._guesser.get_guesses())
        # self._terminal_service.write_text(self._parachute.get_parachute())
        while self._is_playing:
            self._word_line(self._word_generator.get_split_generated_word(), self._guesser.get_guesses())
            self._terminal_service.write_text(self._parachute.get_parachute())
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _get_inputs(self):
        """Accepts a new guess from the user.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._terminal_service.read_text("\nGuess a letter [a-z]:  \n")
        self._guesser.collect_guesses(guess)


    def play_again(self):

        playing_answer = self._terminal_service.read_text("\nWould you like to play again? [y/n]: ")
        if playing_answer.lower() == "y":
            self._is_playing = True
            self._word_generator = Word_generator()
            self._guesser = Guesser()
            self._terminal_service = TerminalService()
            self._parachute = Parachute()
            self._guesser.reset_guesses()
            self._parachute.reset_cut_strings()
        else:
            self._terminal_service.write_text("Thanks for playing!")
            self._is_playing = False
        
    def _do_updates(self):
        """Updates the parachute and the word line following guesses.

        Args:
            self (Director): An instance of Director.
        """
        if self._guesser.get_guesses()[-1] not in self._word_generator.get_generated_word():
            self._parachute.cut_string()

        if self._parachute.get_cut_strings() >= 5:
            print()
            print("Sad! You lose! :(")
            self.play_again()
        
    def _do_outputs(self):
        """Prints an instance of the Parachute.

        Args:
            self (Director): An instance of Director.
        """

        self._word_line(self._word_generator.get_split_generated_word(), self._guesser.get_guesses())

        self._terminal_service.write_text(self._parachute.get_parachute())

    def _word_line(self, word_letters, guess_list):
        
        word_display = ""
        for letter in word_letters:
            if letter in guess_list:
                word_display += f" {letter}"

            else:
                word_display += " _"

        self._terminal_service.write_text(word_display)

        if " _" not in word_display:
            print()
            print("Yay! You are a winner! :)")
            self.play_again()
            self._word_generator = Word_generator()
            self._guesser = Guesser()
            self._terminal_service = TerminalService()
            self._parachute = Parachute()
            self._guesser.reset_guesses()
            self._parachute.reset_cut_strings()
        
        

    
