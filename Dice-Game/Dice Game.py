import random   #Importing Libraries
import csv
from random import randint

#Function to display menu
def DisplayMenu():
    print("_"*80)#Used to separate from other stuff for clarity
    print("1. Play")
    print("2. Highscores")
    print("3. Exit")
#Main Menu Where you choose which action to do next
def ChooseOptions():
    DisplayMenu()
    print("_"*80) #Used to separate from other stuff for clarity

    #Declaring that command is the user's input
    command = input("Choose an Action:").lower()
    print("_"*80) 

    #Comparing the command with strings for each function and going to their respective functions
    if command == "play":
        PlayGame()
        print("_"*80) #Used to separate from other stuff for clarity
    if command == "highscores":
        DisplayWinner()
        print("_"*80)
        ChooseOptions()
    if command == "exit":
        print("Thanks for playing")
    else:
        print("Command not Found.")
        ChooseOptions()  
#Function to read from Csv file of highscores to display Winners
def DisplayWinner(): 
    with open("Highscores.csv", 'r') as Highscores:
        csv_reader = csv.reader(Highscores)
        for line in csv_reader:
            print(line)
def PlayGame():
    #Declaring Variables
    score_1 = 0
    score_2 = 0 
    #Placeholders for while loops
    b = 0
    p = 0 
    #Asking for usernames for each player
    player1 = input("Player 1 Username: ")
    player2 = input("Player 2 Username: ")  
    #Main Program
    #While Loop to have only 5 rounds  
    while b < 5:

        #PLAYER 1 STARTS HERE
        print(player1,"'s turn")
        if input("Type Roll to roll your dice:").lower() == "roll":
            print("_"*80)
            #Declaring the dicerolls are a random integer between 1 and 6
            Player1FirstRoll = randint(1,6)
            Player1SecondRoll = randint(1,6)
            print("You rolled a", Player1FirstRoll, "and a", Player1SecondRoll, "!")
            #Adding the score for each dice to the total
            score_1 += Player1FirstRoll
            score_1 += Player1SecondRoll
            #Checking if Dicerolls are equal to give extra roll
            if Player1FirstRoll == Player1SecondRoll:
               if input("Type Roll to roll your extra dice:").lower() == "roll":
                  ExtraRollPlayer1 = randint(1,6)
            else:
                  ExtraRollPlayer1 = 0
            if ExtraRollPlayer1 != 0:
                print("_"*80)
                print("You rolled an extra", ExtraRollPlayer1)
            RoundTotal = Player1FirstRoll + Player1SecondRoll + ExtraRollPlayer1
            #Checking if total is Even or Odd to take away or give points
            if RoundTotal % 2 == 0:
                score_1 += 10
                print("Extra 10 points for rolling even")
            else:
                score_1 -= 5
                print("Minus 5 points for rolling odd")
            if score_1 < 0:
                score_1 = 0
            score_1 += ExtraRollPlayer1
            print(player1," score is", score_1)
        print("_"*80)       

        #PLAYER 2 STARTS HERE 
        print(player2,"'s turn")        
        if input("Type Roll to roll your dice:").lower() == "roll":
            print("_"*80)
            #Declaring the dicerolls are a random integer between 1 and 6
            Player2FirstRoll = randint(1,6)
            Player2SecondRoll = randint(1,6)
            print("You rolled a", Player2FirstRoll, "and a", Player2SecondRoll, "!")
            #Adding the score for each dice to the total
            score_2 += Player2FirstRoll
            score_2 += Player2SecondRoll
            #Checking if Dicerolls are equal to give extra roll
            if Player2FirstRoll == Player2SecondRoll:
               if input("Type Roll to roll your extra dice:").lower() == "roll":
                  ExtraRollPlayer2 = randint(1,6)
            else:
                  ExtraRollPlayer2 = 0
            if ExtraRollPlayer2 != 0:
                print("_"*80)
                print("You rolled a", ExtraRollPlayer2)
            RoundTotal2 = Player2FirstRoll + Player2SecondRoll + ExtraRollPlayer2
            #Checking if total is Even or Odd to take away or give points
            if RoundTotal2 % 2 == 0:
                score_2 += 10
                print("Extra 10 points for rolling even")
            else:
                score_2 -= 5
                print("Minus 5 points for rolling odd")
            if score_2 < 0:
                score_2 = 0
            score_2 += ExtraRollPlayer2
            print(player2," score is", score_2)
        print("_"*80)       
        #Adding to the count so the loop progresses
        b += 1
        #Checking if count is 5 yet to check who won
        if b == 5:  
                    #Comparing Scores

                    #Player 1 Win
                    if score_1 > score_2:
                      print(player1, "won!") 
                      with open("Highscores.csv", 'a') as Player1Score:
                         csv_writer = csv.writer(Player1Score)
                         csv_writer.writerow([player1, score_1])
                    #Player 2 Win
                    elif score_2 > score_1:
                      print(player2, "won!")
                      with open("Highscores.csv", 'a') as Player2Score:
                         csv_writer2 = csv.writer(Player2Score)
                         csv_writer2.writerow([player2, score_2])
                    #Tie so each player has an extra roll until one gets higher
                    if score_1 == score_2:
                        #While loop so it keeps going until one gets higher
                         while p < 2:
                              print("Tie")
                              print("Roll one more dice to find out who wins!")
                              print("_"*80)  
                              print(player1,"'s turn")
                              if input("Type Roll to roll your dice:").lower() == "roll":
                                    print("_"*80)
                                    tiebreaker1 = randint(1,6)
                                    score_1 += tiebreaker1
                                    print(player1, "rolled a", tiebreaker1, "!")
                              print("_"*80)
                              print(player2,"'s turn")
                              if input("Type Roll to roll your dice:").lower() == "roll":
                                    print("_"*80)
                                    tiebreaker2 = randint(1,6)
                                    score_2 += tiebreaker2
                                    print(player2, "rolled a", tiebreaker2, "!")
                              print("_"*80)
                              if score_1 > score_2:
                                   print(player1, "won!")
                                   break
                              if score_1 < score_2:
                                   print(player2, "won!")
                                   break
                              elif score_1 == score_2:
                                   p = 1                    
    print("@"*80)
    ChooseOptions()

ChooseOptions()
