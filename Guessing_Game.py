# Imports random
import random
# Imports os
import os


# global     
random_list = ["Tomato", "Classroom", "Cheetos", "Lamp", "Car", "Boat"]

# This takes the list and randoms it and assigns it to the var of "secret_word"
secret_word = random.choice(random_list)

def main():
    #Prints Main Stuff
    print("------------------------------")
    print("Welcome To Guessing Game!\n")
    print("Your Given 6 Opitons you must guess which one is Correct!\n")
    print("With Only 3 Tries\n")
    print("------------------------------")
    # Waits for User Input to Continue
    input("Click Any Key To Continue")
    # Clears the terminal
    os.system('cls')
    
    random.shuffle(random_list)
    print("Your Hints are..." + str(random.sample(random_list, len(random_list))))
    
    input("Click Any Key To Continue")
    os.system("cls")
    
    # Goes to Game Function
    game()

def game():
    # Variables
    # This is the secret word | Remember this is a list! | Each must seperated
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    guess = ""
    
# guess is not equal to secret_word do this..
    while guess != secret_word and not(out_of_guesses):
        
        if guess_count < guess_limit:
        # Stores the users Guess
            guess = input("Enter Your Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True 
    if out_of_guesses:
        print("Out of Guesses, You Lose")
        PlayAgain()
    else:
        print("You Win!")
        PlayAgain()

# Last Function if you want to exit or play again!
def PlayAgain():
    print("Would you like to play again?")
    #the var answer stores the input 
    answer = input("Type Yes or No: ")
    # answer must be "Yes" or "No" | If not it will loop back
    while answer not in ["Yes", "No"]:
        print("Invalid input. Please type Yes or No.")
        # Reprints to Screen
        answer = input("Type Yes or No: ")
    if answer == "Yes":
        main()
    else:
        exit()

main()