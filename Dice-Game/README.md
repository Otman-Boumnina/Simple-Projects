# Dice-Game
Simple Command Line 2 Player Dice Game made for a school project.
_________________________________________________________________
## Rules
I made this game with python for 2 players to play. Each player rolls two dice and add the two dice's number together to their score.
If your total is an odd number you lose 5 points, If it is even you get 10 extra points. If both the dice roll the same number you get an extra roll. Once the game is over the person who won get their username and score put into the highscores in an external file (I am using a .csv). When in menu and want to view Highscores, display only top 5 -**TODO** Whoever has the most score after 5 rounds wins
## Libraries used
Random - For Dice Rolls

Csv - For writing and reading from the file
_________________________________________________________________
## To-Do
Make Highscores display only top 5 from the file

Make winner only be put in highscores if better than someone in top 5

Fix Csv file bug where it puts a line between each one with [] example:
```
[User1, User1Score]
[]
[User2, User2Score]
```

Create Flowchart and do testing (Required by school)
