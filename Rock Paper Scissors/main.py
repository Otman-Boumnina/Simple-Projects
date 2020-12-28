import random
choices = [1,2,3]

def computerAI():
    global computerChoice
    computerChoice = random.choice(choices) 
    return computerChoice


def playerChoice():
    global userChoiceInt 
    userChoice = input(str("Rock Paper or Scissors?")).lower()
    if userChoice == "r" or userChoice == "rock":
        userChoiceInt = 1
        return userChoiceInt
    if userChoice == "p" or userChoice == "paper":
        userChoiceInt = 2
        return userChoiceInt
    if userChoice == "s" or userChoice == "scissors":
        userChoiceInt = 3
        return userChoiceInt

def computerWin():
    print("Computer Won. Bad Luck")
    print("-"*80)
    tryAgain = input("Would you like to play again?").lower()
    if tryAgain == "yes" or "y":
        tryAgain = " "
        playGame()
 
def playerWin():
    print("Congratulations! You won.")
    print("-"*80)
    tryAgain = input("Would you like to play again?").lower()
    if tryAgain == "yes" or "y":
        tryAgain = " "
        playGame()

def tie():
    print("It's a tie.")
    print("-"*80)
    tryAgain = input("Would you like to play again?").lower()
    if tryAgain == "yes" or "y":
        tryAgain = " "
        playGame()    

def playGame():
    computerAI()
    playerChoice()
    compareChoices()

def compareChoices():
    if computerChoice == 1 and userChoiceInt == 2:
        playerWin()
    if computerChoice == 2 and userChoiceInt == 1:
        computerWin() 
    if computerChoice == 2 and userChoiceInt == 3:
        playerWin()
    if computerChoice == 3 and userChoiceInt == 2:
        computerWin()
    if computerChoice == 1 and userChoiceInt == 3:
        computerWin()
    if computerChoice == 3 and userChoiceInt == 1:
        playerWin()
    if computerChoice == userChoiceInt:
        tie()

playGame()