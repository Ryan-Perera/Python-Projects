from words import get_word
from text_assets import *
import os
os.system("cls") # To clear terminal

"""
This is Hangman

Difficulty -> Easy (4-5 letter words), Medium (6-7 letter words), Hard (8 letters and above)

"""

def main():
    title()

    # Selecting difficulty and a word
    while True:
        difficulty = input("Enter your desired difficulty: EASY, MEDIUM, HARD: ")
        if difficulty.upper() in ['EASY', 'MEDIUM', 'HARD']:
            word, type, meaning = get_word(difficulty.upper())
            break
        else: 
            print("Incorrect choice. Please re-enter\n")
    

    guesses = []
    done = False
    hint_given = False
    lives = 0

    while not done:
        
        print(draw_hangman(lives))

        for letter in word:
            if letter.lower() in guesses:
                print(letter + " ", end=" ")
            else:
                print("_ ", end=" ")
        print("\n")
        guess = input(f"Remaining Lives {7-lives}, Next Guess: ")
        

        if guess.lower() in guesses:
            print("You've already guesses that letter before. Enter a new letter")
            continue
        else:
            guesses.append(guess.lower())
        
        # if user input not in the word, deduct a life
        if guess.lower() not in word.lower():
            lives = lives + 1
            if hint_given == False:
                help = input("Oops! You just lost a life. You you want a hint? (Y/N)")
                if help.upper() == 'Y':
                    print(f"Here's the defenition of the secret word: {type}, {meaning}") 
                    hint_given = True
            if lives == 6: 
                print(draw_hangman(lives))
                break 
        
        done = True 
        for letter in word: 
            if letter.lower() not in guesses: 
                done = False 

    if done: 
        print(f"Youve found the word! It was {word}")
    else: 
        print(f"Game Over! It was {word}")


if __name__ == "__main__":
    main()
