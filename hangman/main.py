#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:24:14 2020
@author: fernar1
@desc: code for hangman game
"""

from appJar import gui
from hangman import Hangman

 #--------------------------Begin Class MainAppJar-----------------------------
   
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
    
    _tup_images = ('1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif', \
                   '7.gif')
    
    
    def _enable_disable_char_btns(self, enable=True):
        for lst_char_line in self._tup_char_lists:
            for char in lst_char_line:
                if enable:
                    self._app.enableButton(char)
                else:
                    self._app.disableButton(char)
        
    
    def _display_result(self):
        if self._hg.get_result():
            self._app.setLabel('lbl_result', 'You Win!!!')
        else:
            self._app.setLabel('lbl_result', 'You Lose!!!')
            self._app.setLabel('lbl_word', self._hg.guess_word)
    
    
    def _word_sel(self, button):
        if self._hg.process_guess(button.lower()) == True:
            self._app.setLabel('lbl_word', ' '.join(self._hg.lst_guess))
        else:
            self._app.setImage('img_hangman', self. \
                               _tup_images[self._hg.num_guess])
        
        self._app.disableButton(button)
        
        if self._hg.guess_remain() < 1:
            self._display_result() 
            self._enable_disable_char_btns(False)
                           
     
    def _btn_ctrls_clicked(self, button): 
        if button == 'New Word':
            self._hg.init_data()
            self._app.setLabel('lbl_word', ' '.join(self._hg.lst_guess))
            self._app.setImage('img_hangman', self._tup_images[6])
            self._app.setLabel('lbl_result', '')
            self._enable_disable_char_btns(True)
        else:
            self._app.stop()
            
        
    def _init_gui(self):
        self._app = gui('Hangman', '600x600')
        self._app.setBg('slategrey')
        self._app.setFont(12)
        
        self._app.setImageLocation('./images')
        self._app.addImage('img_hangman', self._tup_images[6])
        
        self._app.addLabel('lbl_result', '')
        
        self._app.addLabel('lbl_word', ' '.join(self._hg.lst_guess)). \
            config(font='Helvetica 40')
        
        for lst_char_line in self._tup_char_lists:
            self._app.addButtons(lst_char_line, self._word_sel)

        self._app.addHorizontalSeparator(colour='black')
        self._app.buttons(['New Word', 'Quit'], self._btn_ctrls_clicked, \
                          width=20)
        

    def __init__(self):
        self._hg = Hangman()
        self._init_gui()
        self._app.go()
        

#---------------------------End Class MainAppJar-------------------------------
        
if __name__ == "__main__":
    app = MainAppJar()
 