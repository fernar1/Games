#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:18:56 2020
@author: fernar1
@desc: code for classsic rock paper scissors game
"""

import random


def process_user_choice(user_choice):
        
    comp_rock_results = {
                'Rock': 'Tied',
                'Paper': 'Win',
                'Scissor': 'Lose'
            }
    
    comp_paper_results = {
                'Rock': 'Lose',
                'Paper': 'Tied',
                'Scissor': 'Win'
            }
    
    comp_scissor_results = {
                'Rock': 'Lose',
                'Paper': 'Win',
                'Scissor': 'Tied'
            }
    
 
    if  user_choice not in comp_rock_results:
        raise ValueError('User choice is beyond range')
        
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        print ('Computer chooses Rock')
        result = comp_rock_results[user_choice]
    elif comp_choice == 2:
        print ('Computer chooses Paper')
        result = comp_paper_results[user_choice]
    else:
        print ('Computer chooses Scissor')
        result = comp_scissor_results[user_choice]
    
    return result
    

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
                result = process_user_choice(user_menu[user_choice])
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
    

