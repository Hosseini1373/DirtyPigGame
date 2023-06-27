# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:00:51 2021

@author: sayye
"""
# -*- coding: utf-8 -*-
import board
import init
import schluss
import os
import random

from testing import test_the_whole_game
from testing import test_init



## @brief die main Funktion von project p3
#  @return None
def main():
    continue_playing="y"
    #bis der Spieler möchte und ja sagt, eine Runde von vorne spielen
    while continue_playing=="y":
        board.white_board() 
        n=2#default wert von Anzahl Spieler
        #Wenn test_mode_3 gesetzt ist, wöhlen wir für anzahl Spieler random Werte
        if test_the_whole_game.test_mode_3==True and test_the_whole_game.test_mode==True:
            n=random.choice([2,3,4])
        else:
            n=board.nspieler()#number of players
        game=init.init_spiel(n)#initialazing the game dictionary according to n
        #Für testen in test_mode_2, initializieren wir das Spiel anders:
        if (test_the_whole_game.is_test_2_mode()):
            game=test_init.init_spiel(n)  
        continue_playing=schluss.schluss(game)
    #Console leeren
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()





































                



