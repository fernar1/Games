#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:18:56 2020
@author: fernar1
@desc: code for classic rock paper scissors game
"""

import random
import tkinter as tk


def process_user_choice(user_choice):
    rock_result_list = [    
            {
                'Rock': 'Tied',
                'Paper': 'Win',
                'Scissor': 'Lose'
            },
    
            {
                'Rock': 'Lose',
                'Paper': 'Tied',
                'Scissor': 'Win'
            },
    
            {
                'Rock': 'Win',
                'Paper': 'Lose',
                'Scissor': 'Tied'
            }
    ]
    
    comp_choice_lst = ['rock', 'paper', 'Scissor']
    
    if  user_choice not in rock_result_list[0]:
        raise ValueError('User choice is beyond range')
        
    comp_choice = random.randint(0,2)
    return rock_result_list[comp_choice][user_choice], \
    comp_choice_lst[comp_choice]
    
   
class MainApp():
    
    _modes = [
        ('Rock', 'Rock'),
        ('Paper', 'Paper'),
        ("Scissor", 'Scissor')
    ]
    
    def _create_main_window(self):
        self._main_window = tk.Tk()
        self._main_window.title('Rock Paper Scissor')
        self._main_window.resizable
        
        
    def _create_frame(self):
        self._frame = tk.Frame(self._main_window)
        self._frame.pack()
        
        
    def _create_radio_choice(self):
        choice_label = tk.Label(self._frame, text="Select your choice:",
                                fg='Green')
        choice_label.pack()        
        
        self._var_choice = tk.StringVar()
        self._var_choice.set("Rock") # initialize
        
        for text, mode in self._modes:
            rad_choice = tk.Radiobutton(self._frame, text=text,
                    variable=self._var_choice, value=mode)
            rad_choice.pack(anchor=tk.W)
            
            
    def _create_lbl_status(self):
        self._lbl_comp = tk.Label(self._main_window, text="", width=25,
                                  height=10, fg='Green')
        self._lbl_comp.pack()
        
        self._lbl_result = tk.Label(self._main_window, text="", width=10,
                                    height=10, fg='Green')
        self._lbl_result.pack()
    
    
    def _create_btn_ctrl(self):
        self._btn_play = tk.Button(self._main_window, text='Play', width=25,
                                   command=self._play_clicked)
        self._btn_play.pack(side=tk.LEFT)
        self._btn_quit = tk.Button(self._main_window, text='Quit', width=25,
                                   command=self._main_window.destroy)
        self._btn_quit.pack(side=tk.LEFT)
        
    
    def _play_clicked(self):
        result, comp_choice = process_user_choice(self._var_choice.get())
        self._lbl_comp['text'] = 'The computer chooses {0}'.format(comp_choice)
        self._lbl_result['text'] = 'You {0}'.format(result)
        
                
    def __init__(self):
        self._create_main_window()
        self._create_frame()
        self._create_radio_choice()
        self._create_lbl_status()
        self._create_btn_ctrl()
        self._main_window.mainloop()
        
        
        
if __name__ == "__main__":
    app = MainApp()
    

