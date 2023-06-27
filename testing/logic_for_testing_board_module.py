# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:11:21 2021

@author: sayye
"""
import board



card_type=["Sauberschwein","Drecksau","Matschkarten", "Regenkarten","Stallkarten","Blitzkarten", 
        "Blitzableiterkarten", "Bauer-schrubbt-die-Sau-Karten", 
        "Bauer-ärgere-dich-Karten","Leer","Unbekannt"]



#Todo:

def step(game):
    board.log_spiel("Spieler 0-->   jklfsjkjfklsjdkfjslkd fsjkd fsdklj fksjdk fjsdkl fjklsdj fksjd kfj sdlkjf skd sdjfk sdjklf  sdkfjskldjfksjdklfjskldjflks sdlkjfsjdkl")
    board.log_spiel("Spieler 1-->   jklfsjkjlsjdkfjslkd fsjkd fsdklj fksjdk fjsdkl fjklsdj fksjd kfj sdlkjf skd sdjfk sdjklf sjdkl dsflksjd klfj sdkljfklsjd klfsjdklfj sdkfjskldjfksjdklfjskldjflks sdlkjfsjdkl")
    board.log_spiel("Spieler 2-->   jklfsjksjdkfjslkd fsjkd fsdklj fksjdk fjsdkl fjklsdj fksjd kfj sdlkjf skd sdjfk sdjklf sjj sdkfjskldjfksjdklfjskldjflks sdlkjfsjdkl")
    board.log_spiel("Spieler 3-->   jklfsjkjfklsjdkjslkd fsjkd fsdklj fksjdk fjsdkl fjklsdj fksjd kfj sdlkjf skd sdjfk sdjklf sjdkl dsflksjd klfj sdkljfklsjdkl")
    input_von_spieler=board.INPUT("please write a number of Schweinekarte? --->   ")  
    while(True):
        continue
    
    #Mach etwas mit game dictionary:
    board.draw_board(game,0)
    s="input?"
    input_von_spieler=board.INPUT(s)
    return 1