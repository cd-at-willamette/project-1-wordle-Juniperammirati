########################################
# Name: Juniper Ammirati
# Collaborators (if any): Kendall
# GenAI Transcript (if any): 
# Estimated time spent (hr): 1(day one)
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    def my_guess():
        my_letters = []
        for i in range (5):
            my_letters.append (gw.get_square_letter(0,i))
        print(my_letters)
        my_guess = "".join(my_letters)
        print(my_guess)
        return my_guess
    
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
         if is_english_word (my_guess()):
            gw.show_message ("true")
        else: 
            gw.show_message("not english")



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
