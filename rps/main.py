#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:18:56 2020
@author: fernar1
@desc: code for classic rock paper scissors game
"""

import random


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
                'Rock': 'Lose',
                'Paper': 'Win',
                'Scissor': 'Tied'
            }
    ]
    
    comp_choice_lst = ['rock', 'paper', 'Scissor']
    
    if  user_choice not in rock_result_list[0]:
        raise ValueError('User choice is beyond range')
        
    comp_choice = random.randint(0,2)
    return rock_result_list[comp_choice][user_choice], \
    comp_choice_lst[comp_choice]
   

def main():
    user_menu = {
        1:'Rock',
        2:'Paper',
        3:'Scissor',
        4:'Quit'            
    }
    while True:
        print ('*' * 35)
        print ('Select your choice from the below menu:')
        for key, value in user_menu.items():
            print (key, ':', value)
        try:
            user_choice = int (input ("Please enter your choice:"))
            if (user_choice < 1 or user_choice > 4):
                print ('Input choice is beyond expected range. Please verify' \
                       ' your selection')
                continue
            elif (user_choice == 4):
                break;
            else:
                result, comp_choice = \
                process_user_choice(user_menu[user_choice])
            print ('The computer chooses ' + comp_choice)
            print('You ' + result)
            input('Press any key to continue')
        except ValueError:
            print('Unable to process input. Please verify your selection.')
            continue
        except:
            print('Unexpected error occurred. Exiting the program.')
            break;
            
    return None


if __name__ == "__main__":
    main()
    

