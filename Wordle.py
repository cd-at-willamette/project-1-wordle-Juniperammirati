########################################
# Name:Juniper Ammirati
# Collaborators (if any): Kendall, Tiffany
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import    WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import   ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    def my_guess(): # takes the input and stores it 
        my_letters = []
        for i in range (5):
            my_letters.append (gw.get_square_letter(0,i))
        print(my_letters)
        my_guess = "".join(my_letters)# making the list into a string
        my_guess = my_guess.lower()
        print(my_guess)
        return my_guess
    # one way to solve double letters is to make the answer never have double letters 
    answer = ""
    while len(answer) != 5:
        answer = random.choice(ENGLISH_WORDS) 
    print(answer)
  

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        if is_english_word (my_guess()):
            gw.show_message ("true") # checking if the word input is true 
        else: 
            gw.show_message("not english") # response if word os not in english word import 
        row = gw.get_current_row()
        if my_guess() == answer:
            for column in range (N_COLS):
                gw.set_square_color (row, column, CORRECT_COLOR)
        unmatched = answer 
        if my_guess() != answer: 
            for column in range (N_COLS):
                if my_guess()[column] == answer[column]: 
                    gw.set_square_color(row, column, CORRECT_COLOR)
                    unmatched = unmatched.replace(my_guess()[column]," ", 1)
        if my_guess() != answer:
            for column in range(N_COLS): 
                if my_guess()[column] in unmatched:
                    gw.set_square_color(row, column, PRESENT_COLOR)        
                    unmatched = unmatched.replace(my_guess()[column]," ", 1)
        if my_guess() != answer: 
            for column in range(N_COLS):
                if gw.get_square_color(row, column) == UNKNOWN_COLOR:
                    gw.set_square_color(row,column, MISSING_COLOR)

        
            




# what I need to code for coloring the squares
#def color_square( ):
#define a variable to represnet the as yeat unmatched letters 
# for each letter position in the word 
# if the letter in that position matches hidden word
    # color that square green 
    # take the letter out of the unmatched colletion 
#for each letter position in the word: 
    # if the square in that position is in the unmatched collection:
        # color that square yellow
        # take that letter out of the unmactched collection 
    # else: 
        # color that square gray 



# code that could be used tha Calvin created         
#def redact(word:str, secret:str) -> str:
    #for i in range(len(word)):
        #if word[i] == secret[i]:
            #word = word[:i] + '*' + word[i+1:]
            #DEBUG and print('Redact '+secret[i]+' at '+str(i))
    #return word


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
  
    
    
        



# Startup boilerplate
if __name__ == "__main__":
    wordle()
