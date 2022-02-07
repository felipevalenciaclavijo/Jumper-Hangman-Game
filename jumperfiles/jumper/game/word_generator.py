# this class generates a random word from the self.__words list

import random


class Word_generator:

    def __init__(self):

        
        self.__words = ["final", "price", "hello", "bikes", "trees", "moist", "shard", "enter"]
        self.__generate_word = random.choice(self.__words)

    def get_generated_word(self):

        return self.__generate_word

   
    def get_split_generated_word(self):
        
        generated_word_letters = list(self.__generate_word)
        return generated_word_letters
        
        

    def get_word_length(self):
        return len(self.__generate_word)