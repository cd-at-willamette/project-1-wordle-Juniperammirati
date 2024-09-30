########################################
# Name:Juniper Ammirati
# Collaborators (if any): Kendall, Tiffany  
# GenAI Transcript (if any):
# Estimated time spent (hr): 5
# Description of any added extensions:
########################################

from WordleGraphics import    WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import   ENGLISH_WORDS, is_english_word
import random

def wordle():
    # Grab a random word from the English word list
    answer = ""
    while len(answer) != 5:
        answer = random.choice(ENGLISH_WORDS)
    print(answer)  # checking

    def enter_action():
    
        my_letters = ""  # Set the letters into a string
        for i in range(5):
            my_letters += gw.get_square_letter(gw.get_current_row(), i)
        print(my_letters)  # checking
        my_guess = my_letters.lower()  # Make the word lowercase to match the answer
        print(my_guess)  # check guessed word
        
        # Check if guess is an English word
        if is_english_word(my_guess):
            gw.show_message("English word")  # Check if the word input is English 
            row = gw.get_current_row()  # simplifying getting the row

            # Initialize unmatched as a list of characters from the answer
            unmatched = list(answer)  # This ensures tracking of unmatched letters

            if my_guess == answer:
                # If the guess is correct, color all squares green
                for column in range(N_COLS):
                    gw.set_square_color(row, column, CORRECT_COLOR)
            else:
                # Check for correct letters in the correct position
                for column in range(N_COLS):
                    if my_guess[column] == answer[column]:
                        gw.set_square_color(row, column, CORRECT_COLOR)
                        unmatched[column] = None  # Mark this position as matched

                # Check for correct letters in the wrong position
                for column in range(N_COLS):
                    if my_guess[column] in unmatched:
                        # Find the first occurrence of the letter in unmatched
                        index = unmatched.index(my_guess[column])
                        if unmatched[index] is not None:  # Check if the letter is unmatched
                            gw.set_square_color(row, column, PRESENT_COLOR)
                            unmatched[index] = None  # Mark this letter as matched

                # Color the rest of the letters gray
                for column in range(N_COLS):
                    if gw.get_square_color(row, column) == UNKNOWN_COLOR:
                        gw.set_square_color(row, column, MISSING_COLOR)

            # Color the keys based on the guess
            for i in range(N_COLS):
                letter = my_guess[i]  # Simplify
                color = gw.get_square_color(row, i)  # Simplify what coloring keys is
                if color == CORRECT_COLOR:  # Check if the letter is green in Wordle and apply to keys
                    gw.set_key_color(letter, CORRECT_COLOR)  # Set the color
                elif color == PRESENT_COLOR:
                    if gw.get_key_color(letter) != CORRECT_COLOR:
                        gw.set_key_color(letter, PRESENT_COLOR)
                else:
                    if gw.get_key_color(letter) == UNKNOWN_COLOR:
                        gw.set_key_color(letter, MISSING_COLOR)

            gw.set_current_row(gw.get_current_row() + 1)  # Move to the next row

            if my_guess == answer:
                gw.show_message("YOU WON!!")  # If they won this will appear
                gw.set_current_row(N_ROWS)  # Stops them from typing
            elif gw.get_current_row() == N_ROWS:  # Stops them from moving forward
                gw.show_message("YOU LOST")  # Will appear if they lose
        else:
            gw.show_message("not english")  # Response if the word is not in English

        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
  
    
# Startup boilerplate
if __name__ == "__main__":
    wordle()
