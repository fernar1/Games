#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:24:14 2020
@author: fernar1
@desc: code for hangman game
"""

from appJar import gui
from hangman import Hangman
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
        
    
#-----------------------------------------------------------------------------    
if __name__ == "__main__":
    MainAppJar()