#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:24:14 2020
@author: fernar1
@desc: code for hangman game
"""

import random

words = ['abruptly', 'absurd', 'abyss', 'affix', 'avenue']

def main():
    word = words[random.randint(0, 4)]
    num_guess = 6
    lst_guess = ['_' for i in range(0, len(word))]
    
    while (num_guess > 0):
        print('Guesses left {}\n'.format(num_guess))
        print(' '.join(lst_guess))
        guess_char = input('Enter your guess:')
        if not guess_char.isalpha() or len(guess_char) > 1:
            print('Please enter only one alaphabet as your guess.')
            input('Press any key to continue.')
            continue
        if guess_char in word:
            start = 0
            while True:
                index = word.find(guess_char, start)
                if index == -1:
                    break
                else:
                    lst_guess[index] = guess_char
                    start = index + 1
                    if '_' not in lst_guess:
                        num_guess = -1
        else:
            print ('Incorrect guess!!!')
            input('Press any key to continue.')
            num_guess-= 1
            
    if num_guess == 0:
        print('You Lose!!!')
        print('The correct word was {}'. format(word))
    else:
        print('You WIN!!!')
 

if __name__ == "__main__":
    main()