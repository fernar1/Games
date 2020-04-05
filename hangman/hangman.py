# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:21:35 2020
@author: fernar1
@desc: Code that encapsulates the Hangman game logic
"""
import random
import decorators

class Hangman():
    """
    Class that encapsulates the logic for the hangman game
    """
    def __init__(self):
        self.init_data()
        
    
    def init_data(self):
        """
        Reads a random word from the hangman.txt file and also
        initalizes the data variables for new round
        """
        self._num_guess = 6
        
        with open('hangman.txt') as f:
            lines = f.read().splitlines()
            self._word = lines[random.randint(0, len(lines) - 1)]
            self._lst_guess = ['_' ] * len(self._word)
        
   
    @property
    def guess_word_len(self):
        """
        The length of the word that needs to be guessed
        """
        return len(self._word)

    
    @property
    def guess_word(self):
        """
        The word that needs to be guessed
        """
        return self._word

    
    @property
    def num_guess(self):
        """
        The number of guesses remaining
        """
        return self._num_guess


    @num_guess.setter
    def num_guess(self, num_guess):
        self._num_guess = num_guess

    
    @property
    def lst_guess(self):
        """
        Variable that contains the guessed letters
        """
        return self._lst_guess

    
    def guess_remain(self):
        """
        Function to check if guesses are remaining
        Returns True, if guesses are remaining otherwise false
        """
        return self._num_guess > 0


    @decorators.is_single_alphabet((1,))
    def process_guess(self, guess_char):
        """
        Function process the guess from the user and validates if it is
        in the word that needs to be guessed.
        """
        match_found = True
        if guess_char in self._word:
            self._replace_guess_char(guess_char)
        else:
            self.num_guess -= 1
            match_found = False
        return match_found

    
    def _replace_guess_char(self, guess_char):
        start = 0
        while True:
            index = self._word.find(guess_char, start)
            if index == -1:
                break
            else:
                self._lst_guess[index] = guess_char
                start  = index + 1
                if '_' not in self._lst_guess:
                    self.num_guess = -1

                    
    def get_result(self):
        return self.num_guess == -1
