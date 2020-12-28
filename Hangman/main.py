import random
from words import words
import string
 
def getValidWord(words):
    word = random.choice(words)
    while "-" or " " in word:
        word = random.choice(words)
        return word.upper()

def hangMan(): 
    word = getValidWord(words) 
    wordLetters = set(word) 
    alphabet = set(string.ascii_uppercase) 
    usedLetters = set()

    lives = 6
    
    while len(wordLetters) > 0 and lives > 0:
        print("-"*80)
        print(f"You have {lives} lives left")
        print("You have used the letters: ", " ".join(usedLetters), "\n")

        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print("Current Word is: ", "-".join(wordList))

        userLetter = input("Guess a letter:").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print("Correct")
            elif userLetter not in wordLetters:
                print("-"*80)
                print("Incorrect, you lost a life")
                lives -= 1
        elif userLetter in usedLetters:
            print("-"*80)
            print("You have already typed in that character. Please Try Again")
        else:   
            print("-"*80)
            print("Invalid Character. Please Try Again")
 
hangMan() 