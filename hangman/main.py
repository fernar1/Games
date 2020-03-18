#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:24:14 2020
@author: fernar1
@desc: code for hangman game
"""

import random

class hangman():
    _words = ['abruptly', 'absurd', 'abyss', 'affix', 'avenue']
    
    
    def __init__(self):
        self._word = self._words[random.randint(0, 4)]
        self._num_guess = 6
        self._lst_guess = ['_' ] * len(self._word)
    
    @property
    def guess_word_len(self):
        return len(self._word)
    
    @property
    def guess_word(self):
        return self._word
    
    @property
    def num_guess(self):
        return self._num_guess

    @num_guess.setter
    def num_guess(self, num_guess):
        self._num_guess = num_guess
    
    @property
    def lst_guess(self):
        return self._lst_guess
    
    def guess_remain(self):
        return self._num_guess > 0
    
    def process_guess(self, guess_char):
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
    

def main():
    hg = hangman()
       
    while (hg.guess_remain() > 0):
        print('Guesses left {}\n'.format(hg.num_guess))
        print(' '.join(hg.lst_guess))
        guess_char = input('Enter your guess:')
        try:
            if hg.process_guess(guess_char) == False:
                print ('Incorrect guess!!!')
                input('Press any key to continue.')
        except ValueError:
            print('Please enter only one alaphabet as your guess.')
            input('Press any key to continue.')
            
    if hg.get_result():
        print('You WIN!!!')       
    else:
        print('You Lose!!!')
        print('The correct word was {}'. format(hg.guess_word))
        
 

if __name__ == "__main__":
    main()