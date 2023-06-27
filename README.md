# Implementing Dreckschwein game in python with Colorama interace


# What the project does
p3.py is the card game "Dreckschwein" programmed with python. For visualization colorama was used.
## Our Extension to the game:
As an extension we decided to add a new card to the deck, the name of the card is **Blitzableiter Gold**. This card is an altered version of the standard **Blitzableiter** it has the same function but additionally it allows the player to play another card after using the **Blitzableiter Gold** effectively allowing the player to play two cards in a turn instead of one. One can not also put this card on **Blitzableiter**. We can also not put **Blitzableiter** on **Blitzableiter Gold**
Anzahl von **Blitzableiter Gold** Karten ist 2.



# How users can get started with the project
**To have the best playing experience, the user is advised to use a screen resolution of 1920x1080 pixels with scaling set to 100% in Windows.**

Input and Output of this application is over the Console. This app can be run 
by using the command **python p3.py** in console.

Because the game can be played with 2, 3 or 4 players, the user is first asked to input the amount of players that are participating in the match. After setting the desired amount of players, the playing board will be created according to the amount of players.

The game starts with waiting for input of Player_0. So each player has a number ranging from [0, #players - 1]. Each card stack has also a number. All these numbers are visible on the screen. Below the Game panel, the questions will be asked, which control the flow of game by the players. On the right-hand side of the panel, there will 
be a logging panel. Every move by the players will be logged on the logging panel. Also, illegal moves by the players will be shown there. For more information on how to play the game, check out the file: docs/DS.PM1-03-Drecksau-Anleitung.pdf 







# Files
The project is divided into multiple files:

### p3.py

p3.py is the main file of the project and is used to start the game out of the console. It imports multiple sub-files such as board.py, init.py, schluss.py, test_the_whole_game.py and test_init.py. These files will get explained more precisely in the following paragraphs.
It also contains a shuffled deck of cards.

### init.py
init.py is the whole backbone of the project it contains the dictionary "game" where the logic.py (logic) file takes and writes information into, for the board.py (UI) file to know what information to display onto the screen. "game" dictionary is also initialized in this module. "game" dictionary is essentially the interface
between board and logic module.  

### logic.py
The logic module contains the whole game logic.
Every card has its own function that can be called. The functions check if the move is possible or not.  
If the move is **possible** it returns a **True** value, it then also discards all the cards that need to be discarded and draws a new card from the deck.
If the move is **not possible** it returns a **False** value and prints the associated error message onto the board log.
The function step() is the main loop, it asks the current player what it wants to do, and the player can simply input his decisions into the console. After every input it is checked if the input was correct, meaning if an integer is asked it also only allows an integer as an answer, else it gives out an error message and asks the user to try again.
In combination with the functions of the cards checking if the move is possible, it is ensured that each player can only make legal moves.
After a player has done his move, it outputs the made move onto the game log and goes to the next player.
After every turn from a player it is checked if there is a winner and if so it breaks out of the loop and returns to the winning player.

### board.py
This Module essentially implements the UI of the game using **Colorama** library. The interface that this UI module offers are: 
**input**, ***draw_board**, **white_board**, **log_spiel** 
#### input function
It gets a string and prints it on the screen. It then takes the input of the player and returns it as return value
#### white_board function
It draws a playing board without any cards. This function is only used in p3.py, in order to initialize the game and wait for the players to enter 
the number of players.
#### draw_board
It gets the "game" dictionary and reflects the changes in the game dynamics that are all saved in the "game" dictionary on the screen. It returns nothing.
#### log_spiel
It gets a string and logs the string in the logging panel 


### test_the_whole_game.py
This module is basically a module to simulate the moves of a player. If you set `test_mode` variable in this file to `True` and then run the program on the console, it
will ask the number of players and after that it goes on to simulate that number of players, without asking any other question. It also shows the progress of each 
simulated player. Each move by a simulated player takes approximately **0.001 seconds** You can change speed Global variable. For more details, see below

#### Drei Modes von Testing:
    MODE 1: test_mode=True and test_mode_2=False and test_mode_3=False
    Simuliert Spiel aber nach Spiel Ende wird gefragt, ob wir mit Simulation 
    weiter machen wollen.
    
    MODE 2: test_mode=True and test_mode_2=True  and test_mode_3=False
    Simuliert Spiel aber nach Spiel Ende wird nicht gefragt, ob wir mit Simulation 
    weiter machen wollen. Es simuliert unendlich mal. Die wahrscheinlichkeiten
    sind auch anders gewichtet-->siehe test_game_2() Funktion
    
    MODE 3: test_mode=True and test_mode_2=False  and test_mode_3=True
    Testet eine spezifische Reihenfolge von Nachziehkarten Staple und wenn es nicht 
    richtig raus kommt, wird es geloggt, dass der Test nicht bestanden ist

### schluss.py
Die Funktion wird ausgeführt, wenn jemand gewonnen hat. 
**y** bedeutet das die Spieler nochmals spielen wollen und
**n** bedeutet, dass sie nicht spielen wollen. Und das beendet das Spiel
und löscht das Board von Console

Wenn wir in test_modus 1 sind fragen wir, ob noch eine Runde simulieren wollen.
wenn wir in test_modus 2 sind fragen wir nicht und machen unendlich weiter




















# Where users can get help with your project
To get more infos on the Project please email us: hossesay@students.zhaw.ch
# Who maintains and contributes to the project
The Collabrotors on this Project are:
Sayyed Ahmad Hosseini

