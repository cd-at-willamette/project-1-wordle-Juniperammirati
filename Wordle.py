########################################
# Name:Juniper Ammirati
# Collaborators (if any): Kendall, Tiffany,  
# GenAI Transcript (if any):
# Estimated time spent (hr): 4.5
# Description of any added extensions:
########################################

from WordleGraphics import    WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import   ENGLISH_WORDS, is_english_word
import random

def wordle():
    answer = ""#grabbing a random work from english word list 
    while len(answer) != 5: # making sure the random word picked to be only 5 letters 
        answer = random.choice(ENGLISH_WORDS) # setting what answer is 
    print(answer)# prints answer in terminal 
  

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        my_letters = "" #sets the letters into a string 
        for i in range (5):
            my_letters += (gw.get_square_letter(gw.get_current_row(),i))
        print(my_letters) #prints 5 letters that were inputted 
        my_guess = my_letters.lower() # makes the word lower to match what the answer would show 
        print(my_guess)#checking  
        # checking if guess is an english word  
        if is_english_word (my_guess):
            gw.show_message ("English word") # checking if the word input is english and returning true 
            row = gw.get_current_row() #setting gw to a simple word for more code 
            
            if my_guess == answer: # checking if the guess is correct and will color green
                for column in range (N_COLS):
                    gw.set_square_color (row, column, CORRECT_COLOR)# if this is true stop
            unmatched = answer # used to store already colored letters 
            if my_guess != answer: # coloring the correct letters and place within a guess  
                for column in range (N_COLS):
                    if my_guess[column] == answer[column]: #checking each letter 
                        gw.set_square_color(row, column, CORRECT_COLOR)# checking letters within row and coloring them green 
            unmatched = unmatched.replace(my_guess[column]," ", 1)# taking out the letters alreayd colored 
            if my_guess != answer: # coloring letters that are correct but in wrong position
                for column in range(N_COLS): 
                    if my_guess[column] in unmatched: # use unmatched to only check letters not colored 
                        gw.set_square_color(row, column, PRESENT_COLOR) # coloring the letters yellow if they are in the word but wrong position     
                        unmatched = unmatched.replace(my_guess[column]," ", 1) # taking out all the yellow colored letters 
            if my_guess != answer: # coloring the rest of the lettters gray 
                for column in range(N_COLS):
                    if gw.get_square_color(row, column) == UNKNOWN_COLOR:#coloring every other letter not colored in wordle grid 
                        gw.set_square_color(row,column, MISSING_COLOR)           
              
            for i in range(N_COLS):
                letter =  my_guess[i]#simplify 
                color= gw.get_square_color(gw.get_current_row(),i)#simplify what coloring keys is 
                if color == CORRECT_COLOR: # checks the letters green in wordle and applying it to the keys 
                    gw.set_key_color(letter,CORRECT_COLOR)# setting the color 
                elif color == PRESENT_COLOR:
                    if gw.get_key_color(letter) != CORRECT_COLOR:
                        gw.set_key_color(letter,PRESENT_COLOR)
                else: 
                    if gw.get_key_color(letter) == UNKNOWN_COLOR:
                        gw.set_key_color(letter, MISSING_COLOR)
            gw.set_current_row(gw.get_current_row()+1)  
            if my_guess == answer:
                gw.show_message("YOU WON!!")# if they won this will appear
                gw.set_current_row(N_ROWS) # stops them from typing 
            elif gw.get_current_row() == N_ROWS:#this will stop them from moving forward 
                gw.show_message("YOU LOST")#will appear if they lose 
        else: 
            gw.show_message("not english") # response if word if not in english word import 
        
       
        


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
  
    
    
        



# Startup boilerplate
if __name__ == "__main__":
    wordle()
