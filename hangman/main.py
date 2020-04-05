#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:24:14 2020
@author: fernar1
@desc: code for hangman game
"""

import random
from appJar import gui

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

    
    def process_guess(self, guess_char):
        """
        Function process the guess from the user and validates if it is
        in the word that needs to be guessed.
        """
        match_found = True
        if not guess_char.isalpha() or len(guess_char) > 1:
            raise ValueError('Invalid guess')            
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
    
#-----------------------------------------------------------------------------    
    
class MainAppJar():
    """
    Class that contains code to display the GUI for the game.
    It uses the appJar library for this purpose
    """
    _tup_char_lists = (
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    )
    
    
    def _display_result(self):
        if self._hg.get_result():
            self._app.setLabel('lbl_guess', 'You Win!!!')
        else:
            self._app.setLabel('lbl_guess', 'You Lose!!!')
            self._app.setLabel('lbl_word', self._hg.guess_word)
    
    
    def _word_sel(self, button):
        if self._hg.process_guess(button.lower()) == True:
            self._app.setLabel('lbl_word', ' '.join(self._hg.lst_guess))
        else:
            self._app.setLabel('lbl_guess', 'Guesses left:{0}' \
                           .format('*' * self._hg.num_guess))
        
        self._app.disableButton(button)
        
        if self._hg.guess_remain() < 1:
          self._display_result()                         
                           
     
    def _btn_ctrls_clicked(self, button): 
        if button == 'New Word':
            self._hg.init_data()
            self._app.setLabel('lbl_word', ' '.join(self._hg.lst_guess))
            self._app.setLabel('lbl_guess', 'Guesses left:{0}' \
                           .format('*' * self._hg.num_guess))
            for lst_char_line in self._tup_char_lists:
                for char in lst_char_line:
                    self._app.enableButton(char)
        else:
            self._app.stop()
            
        
    def _init_gui(self):
        self._app = gui('Hangman', '400x400')
        self._app.setBg('slategrey')
        self._app.setFont(12)
        self._app.addLabel('lbl_guess', 'Guesses left:{0}' \
                           .format('*' * self._hg.num_guess))
        self._app.addLabel('lbl_word', ' '.join(self._hg.lst_guess))
        
        for lst_char_line in self._tup_char_lists:
            self._app.addButtons(lst_char_line, self._word_sel)

        self._app.addLabel('lbl_sep', '-' * 96)
        self._app.buttons(['New Word', 'Quit'], self._btn_ctrls_clicked, \
                          width=20)
        

    def __init__(self):
        self._hg = Hangman()
        self._init_gui()
        self._app.go()
        
    
    
if __name__ == "__main__":
    MainAppJar()