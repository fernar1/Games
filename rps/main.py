#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:18:56 2020
@author: fernar1
@desc: code for classic rock paper scissors game
"""

import random

from appJar import gui


def process_user_choice(user_choice):
    rock_result_list = [
        {"Rock": "Tied", "Paper": "Win", "Scissor": "Lose"},
        {"Rock": "Lose", "Paper": "Tied", "Scissor": "Win"},
        {"Rock": "Win", "Paper": "Lose", "Scissor": "Tied"},
    ]

    comp_choice_lst = ["rock", "paper", "Scissor"]

    if user_choice not in rock_result_list[0]:
        raise ValueError("User choice is beyond range")

    comp_choice = random.randint(0, 2)
    return rock_result_list[comp_choice][user_choice], comp_choice_lst[comp_choice]


class MainAppJar:

    _choices = ["Rock", "Paper", "Scissor"]

    def _init_gui(self):
        self._app = gui("Rock Paper Scissor", "400X400")
        self._app.setBg("slategrey")
        self._app.setFont(18)

    def _create_radio_choice(self):
        self._app.addLabel("lbl_choice", "Select your choice:")
        self._app.setLabelBg("lbl_choice", "blue")
        self._app.setLabelFg("lbl_choice", "orange")

        for choice in self._choices:
            self._app.addRadioButton("rad_choice", choice)
        self._app.setRadioButton("rad_choice", self._choices[0], False)
        self._app.setRadioButtonChangeFunction("rad_choice", self._sel_change)

    def _create_lbl_status(self):
        self._app.addLabel("lbl_comp_choice", "")
        self._app.addLabel("lbl_result_choice", "")

    def _create_btn_ctrl(self):
        self._app.addButtons(["Play", "Quit"], self._btn_clicked)

    def _btn_clicked(self, button):
        if button == "Quit":
            self._app.stop()
        else:
            result, comp_choice = process_user_choice(
                self._app.getRadioButton("rad_choice")
            )
            self._app.setLabel(
                "lbl_comp_choice", "The computer chooses {0}".format(comp_choice)
            )
            self._app.setLabel("lbl_result_choice", "You {0}".format(result))

    def _sel_change(self):
        self._app.setLabel("lbl_comp_choice", "")
        self._app.setLabel("lbl_result_choice", "")

    def __init__(self):
        self._init_gui()
        self._create_radio_choice()
        self._create_lbl_status()
        self._create_btn_ctrl()
        self._app.go()


if __name__ == "__main__":
    app = MainAppJar()
