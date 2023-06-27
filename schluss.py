# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:23:16 2021

@author: sayye
"""
import logic
import board
import random

from testing import test_the_whole_game
from testing import test_init






## @brief Die Funktion wird ausgeführt, wenn jemand gewonnen hat. 
#         y bedeutet das die Spieler nochmals spielen wollen und
#         n bedeutet, dass sie nicht spielen wollen und das beendet das Spiel
#         und löscht das Board von Console
#  @param game game dictionary
#  @return y oder n
def schluss (game):
    gewinner=logic.step(game)    
    board.log_spiel("DER GEWINNER IST SPIERLER NR. "+str(gewinner)+"")
    #Wenn wir in test_modus 1 sind fragen wir, ob noch eine Runde simulieren wollen.
    #wenn wir in test_modus 2 sind fragen wir nicht und machen unendlich weiter
    if test_the_whole_game.test_mode==True and test_the_whole_game.test_mode_3==False:
        test_the_whole_game.test_mode=False
        wish=board.input_ask(game,"Game is ended, Do you want to play again?--> y/n  ")  
        while(True):
            if(wish=="y"):
                test_the_whole_game.test_mode=True
                return "y"
            elif(wish=="n"):
                test_the_whole_game.test_mode=True
                return "n"
            else:
                wish=board.input_ask(game,"False Input, Choose y or n-->  ")
                test_the_whole_game.test_mode=True
    elif(test_the_whole_game.test_mode==True and test_the_whole_game.test_mode_3==True):
        return "y"
    else:
        wish=board.input_ask(game,"Game is ended, Do you want to play again?--> y/n  ")  
        while(True):
            if(wish=="y"):
                return "y"
            elif(wish=="n"):
                return "n"
            else:
                wish=board.input_ask(game,"False Input, Choose y or n-->  ")        
    
            
        