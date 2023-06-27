# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:11:21 2021

@author: sayye
"""
import board
import aux_functions
import random



card_type=["Sauberschwein","Drecksau","Matschkarten", "Regenkarten","Stallkarten","Blitzkarten", 
        "Blitzableiterkarten", "Bauer-schrubbt-die-Sau-Karten", 
        "Bauer-ärgere-dich-Karten","Leer","Unbekannt","Blitzableiterkarten-gold"]





## @brief   dreckschwein is the function for the "Dreckschwein Karte" it allows the
#           player to turn his (by default) "Sauberschwein" into a "Dreckschwein.
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   game directory 
#
#  @details The function needs to meet a few... to allow the card to be used:
#           - It needs to check if the Schwein is not already dirty
#           - It needs to check if the Schwein does exist
#           
#                  
#  @return  If all conditions are fulfilled it returns a True statement else it returns a False
#           statement and prints the according ERROR message onto the board_log.     


def dreckschwein(schwein_nr, game):
    spieler=game["dran_spieler"] 
    anz_schweine = 6-game["anzahl_spieler"]  
    
    #needs to check if the schwein exists
    if schwein_nr <= anz_schweine:
        
        #needs to check if the schwein is not already dirty 
        if "Dreckschwein" not in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
            
            #Ausführen der Karte
            (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr].remove("Sauberschwein")
            (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr].insert(0,"Dreckschwein")
            
            #ablage und ziehen von neuer Karte
            (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Matschkarten")
            (game["ablage_staple"]).append("Matschkarten")
            game=aux_functions.is_nachzieh_staple_full(game)
            (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
            
            #board refresh
            board.draw_board(game)
            
            return True        
            

        else:
            board.log_spiel("ERROR: The Schwein is already dirty")
            return False

    
    else:
        board.log_spiel("ERROR: This Schwein doesn't exist!")
        return False
    
    




## @brief   regenkarte is the function for the "Regen Karte" it allows the
#           player to turn all "Dreckschwein(s)" from ALL players (including himself)
#           into "Sauberschweine". Only "Sauberschweine" who have a "Stall" are 
#           not affected by this card.
#
#  @param   game directory 
#
#  @details The function doesn't need to check for any condition and can be played always.            
#  @return None   
    
    
def regenkarte(game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]
    
    #loop to iterate all "schweine" from all players
    for i in range (game["anzahl_spieler"]):
        for schwein_nr in range(anz_schweine):
            #check if the "Schwein" is dirty
            if "Dreckschwein" in (((game["spielern"])[i])["schwein_karten"])[schwein_nr] and "Stallkarten" not in (((game["spielern"])[i])["schwein_karten"])[schwein_nr]:
                (((game["spielern"])[i])["schwein_karten"])[schwein_nr].remove("Dreckschwein")
                (((game["spielern"])[i])["schwein_karten"])[schwein_nr].insert(anz_schweine,"Sauberschwein")

    
    
    #ablage und ziehen von neuer Karte
    (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Regenkarten")
    (game["ablage_staple"]).append("Regenkarten")
    game=aux_functions.is_nachzieh_staple_full(game)
    (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
    
    #board refresh
    board.draw_board(game)
            





## @brief   stallkarte is the function for the "Stallkarte" it allows the
#           player to turn build a "Stall" onto one of his "Schwein"
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   game directory 
#  @details The function needs to check a few... to allow the card to be used:
#           - It needs to check if the Schwein does not already have a "Stall"
#           - It needs to check if the Schwein does exist
#           
#                       
#  @return  If all are conditions fulfilled it returns a True statement else it returns a False
#           statement and prints the according ERROR message onto the board_log.    


def stallkarte(schwein_nr,game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]
    
    #needs to check if the schwein exists
    if schwein_nr <= anz_schweine:    
        #check if there is not already a Stall installed
        if "Stallkarten" not in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
            
            #Ausführung der Karte
            (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr].append("Stallkarten")
            
            #ablage und ziehen von neuer Karte
            (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Stallkarten")
            (game["ablage_staple"]).append("Stallkarten")
            game=aux_functions.is_nachzieh_staple_full(game)
            (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
            
            #board refresh
            board.draw_board(game)
            
            return True            
            

       
        else:
            
            #ERROR THERE IS ALREADY A STALL INSTALLED
            board.log_spiel("ERROR: There is already a Stall installed")
            return False
    else:
        board.log_spiel("ERROR: This Schwein doesn't exist!")
        return False        
        






## @brief   blitzkarte is the function for the "Blitz Karte".
#           It allows the player to destroy one of the players "Stall"
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   ziel_spieler index of which player should be attacked
#  @param   game directory 
#
#  @details The function needs to meet a few conditions to allow the card to be used:
#           - It needs to check if the "Schwein" does have a "Stall" to destroy
#           - It needs to check if there is a "Blitzbeiter" installed.
#             (The blitzableiter prevents the Stall to be destroyed by a Blitz)
#           - It needs to check if the attacked player exists
#           - It needs to check if the attacked "Schwein" exists
#           
#                     
#  @return  If all are conditions fulfilled it returns a True statement else it returns a False
#           statement and prints the according ERROR message onto the board_log.  



def blitzkarte(schwein_nr,ziel_spieler,game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]
    
    #needs to check if there is a Stall installed
    if schwein_nr <= anz_schweine and ziel_spieler <=  game["anzahl_spieler"] -1 and spieler != ziel_spieler:  
        if "Stallkarten" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]:
            #needs to check if there not already a Blitzableiter installed
            if not("Blitzableiterkarten" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]) and not("Blitzableiterkarten-gold" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]):
                
                if "Bauer-ärgere-dich-Karten" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr] and "Stallkarten" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]:
                    
                    #Ausführen der Karte
                    (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr].remove("Bauer-ärgere-dich-Karten")
                    (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr].remove("Stallkarten")
                    
                    #adding the blitzed cards onto Ablagestapel
                    (game["ablage_staple"]).append("Bauer-ärgere-dich-Karten")
                    (game["ablage_staple"]).append("Stallkarten")
                    
                    #adding the used card onto Abalgestapel
                    (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Blitzkarten")
                    (game["ablage_staple"]).append("Blitzkarten")
                    
                    #drawing a new card
                    game=aux_functions.is_nachzieh_staple_full(game)
                    (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
                    
                    
                    #board refresh
                    board.draw_board(game)
                    
                    return True
                
                if "Stallkarten" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr] and "Bauer-ärgere-dich-Karten" not in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]:
                    
                    #Ausführen der Karte
                    (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr].remove("Stallkarten")
                    
                    #adding the blitzed cards onto Ablagestapel
                    (game["ablage_staple"]).append("Stallkarten")
                    
                    #adding the used card onto Abalgestapel
                    (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Blitzkarten")
                    (game["ablage_staple"]).append("Blitzkarten")
                    
                    #drawing a new card
                    game=aux_functions.is_nachzieh_staple_full(game)
                    (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
                    
                    #board refresh
                    board.draw_board(game)
                    
                    return True                

            
            else:
                board.log_spiel("ERROR There is a Blitzableiter installed")
                return False
                

     

        else:
            board.log_spiel("ERROR: There is no Stall installed to blitz")
            return False
        
        
    else :
        if ziel_spieler == spieler:
            board.log_spiel("ERROR: You can't blitz your own Schwein")
            return False
        
        elif ziel_spieler <= game["anzahl_spieler"]:
            board.log_spiel("ERROR: This player doesn't exist!")
            return False
            
        else:
            board.log_spiel("ERROR: This Schwein doesn't exist!")
            return False  
            
            



## @brief   blitzableiter is the function for the "Blitzableiter Karte".
#           It allows the player to build a "Blitzableiter" onto his "Stall"
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   game directory 
#
#  @details The function needs to meet a few conditions to allow the card to be used:
#           - It needs to check if there is a "Stall" to build a Blitzableiter on
#           - It needs to check if there is already a "Blitzbeiter" installed.
#           - It needs to check if the selected Schwein exists
#           
#                     
#  @return  If all are fulfilled it returns a True statement else it returns a False
#           statement and the according ERROR message onto the board_log.     


def blitzableiter(schwein_nr,game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]
    
    if schwein_nr <= anz_schweine:  
        #needs to check if there is a Stall installed
        if "Stallkarten" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
            #needs to check if there is not already a Blitableiter installed
            if not ("Blitzableiterkarten" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]) and not ("Blitzableiterkarten-gold" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]):
                #Ausführen der Karte
                (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr].append("Blitzableiterkarten")
                
                

                
                #adding the used card onto Ablagestapel
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Blitzableiterkarten")
                (game["ablage_staple"]).append("Blitzableiterkarten")
                
                #drawing a new card
                game=aux_functions.is_nachzieh_staple_full(game)
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
                
                board.draw_board(game)
                
                return True              
            else:
                
                board.log_spiel("ERROR: There is already a Blitzableiter or Blitzkarten_gold installed")
                return False

        
        else:
            board.log_spiel("ERROR: There is not a Stall installed to build a Blitzablieter on")
            return False
    
    else:
        board.log_spiel("ERROR: This Schwein doesn't exist!")
        return False
    

## @brief   blitzableiter is the function for the "Blitzableiter Karte".
#           It allows the player to build a "Blitzableiter" onto his "Stall"
#           It is the same card as the normal "Blitzableiter" but allows the player
#           to directly play another card instead of wainting for the next turn.
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   game directory 
#
#  @details The function needs to meet a few conditions to allow the card to be used:
#           - It needs to check if there is a "Stall" to build a Blitzableiter on
#           - It needs to check if there is already a "Blitzbeiter" installed.
#           - It needs to check if the selected Schwein exists
#           
#                    
#  @return  If all are fulfilled it returns a True statement else it returns a False
#           statement and the according ERROR message onto the board_log.   


def blitzableiter_gold(schwein_nr,game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]
    
    if schwein_nr <= anz_schweine:  
        #needs to check if there is a Stall installed
        if "Stallkarten" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
            #needs to check if there is not already a Blitableiter installed
            if not("Blitzableiterkarten-gold" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]) and not("Blitzableiterkarten" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]):
                
                (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr].append("Blitzableiterkarten-gold")
                
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Blitzableiterkarten-gold")
                (game["ablage_staple"]).append("Blitzableiterkarten-gold")
                game=aux_functions.is_nachzieh_staple_full(game)
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
                
                board.draw_board(game)
                
                return True

            else:
                board.log_spiel("ERROR: There is already a Blitzableiter or Blitzableiter_gold installed")
                return False

        
        else:
            
            board.log_spiel("ERROR: There is not a Stall installed to build a Blitzablieter on")
            return False
    
    else:
        board.log_spiel("ERROR: This Schwein doesn't exist!")
        return False 
    

    
            
## @brief   bauerschrubb is the function for the "Bauer schrubbt die Sau Karte".
#           It allows the player to turn a "Dreckscwein" into a "Sauberschwein"
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   ziel_spieler index of which player should be attacked
#  @param   game directory 
#
#  @details The function needs to meet a few conditions to allow the card to be used:
#           - It needs to check if there is a "Bauer-ärgere-dich-Karten" installed
#           - It needs to check if the selected target is not already a "Sauberschwein".
#           - It needs to check if the selected enemy Player exists
#           - It needs to check if the selected Schwein exists
#           - It needs to check if the player is not attacking himself
#           
#                       
#  @return  If all are fulfilled it returns a True statement else it returns a False
#           statement and the according ERROR message onto the board_log.



def bauerschrubb(schwein_nr, ziel_spieler,game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]
    if schwein_nr <= anz_schweine and ziel_spieler <= game["anzahl_spieler"]-1 and ziel_spieler != spieler:
        
        #needs to check if there is a Bauer-ärgere-dich installed
        if "Bauer-ärgere-dich-Karten" not in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]:
            #needs to check if the Schwein is dirty
            if "Sauberschwein" not in (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr]:
                (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr].remove("Dreckschwein")
                (((game["spielern"])[ziel_spieler])["schwein_karten"])[schwein_nr].insert(0,"Sauberschwein")
                
                
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Bauer-schrubbt-die-Sau-Karten")
                (game["ablage_staple"]).append("Bauer-schrubbt-die-Sau-Karten")
                game=aux_functions.is_nachzieh_staple_full(game)
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
                
                
                board.draw_board(game)
                
                return True

            else:
                board.log_spiel("ERROR: The Schwein is not dirty")
                return False

            
        else:
            board.log_spiel("ERROR: There is a Bauer-ärgere-dich installed")
            return False
    
    else :
        if ziel_spieler == spieler:
            board.log_spiel("ERROR: You can't schrubb your own Schwein")
            return False
        
        elif ziel_spieler <= game["anzahl_spieler"]:
            board.log_spiel("ERROR: This player doesn't exist!")
            return False
        
        else:
            board.log_spiel("ERROR: This Schwein doesn't exist!")
            return False 
            
## @brief   baueraerger is the function for the "Bauer ärgere dich Karte".
#           It allows the player to install a "Bauer ärger dich nicht" into his "Stall"
#           preventing the "Bauer schrubbt die Sau" karte from working
#
#  @param   schwein_nr index of Schwein which the card should be used on
#  @param   game directory 
#
#  @details The function needs to meet a few conditions to allow the card to be used:
#           - It needs to check if there is a "Stall" installed to build a "Bauer ärger dich"
#           - It needs to check if there is not aready a "Bauer ärger dich Karte" installed
#           - It needs to check if the selected Schwein exists
#           
#                    
#  @return  If all are fulfilled it returns a True statement else it returns a False
#           statement and the according ERROR message onto the board_log.        


def baueraerger(schwein_nr,game):
    spieler=game["dran_spieler"]
    anz_schweine = 6-game["anzahl_spieler"]

    if schwein_nr <= anz_schweine: 
        #needs to check if there is a Stall installed
        if "Stallkarten" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
            #needs to check if there is not already a Bauer-ärgere-dich installed
            if "Bauer-ärgere-dich-Karten" not in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
                
                (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr].append("Bauer-ärgere-dich-Karten")
                
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove("Bauer-ärgere-dich-Karten")
                (game["ablage_staple"]).append("Bauer-ärgere-dich-Karten")
                game=aux_functions.is_nachzieh_staple_full(game)
                (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop()) 
                
                
                board.draw_board(game)
                
                return True

            else:
                board.log_spiel("ERROR: There is already a Bauer-ärgere-dich installed")
                return False

        
        else:
            #ERROR THERE IS NOT A STALL INSTALLED TO BUILD A Bauer-ärgere-dich IN
            board.log_spiel("ERROR: There is not a Stall installed to build a Bauer-ärgere-dich")
            return False
    
    else:
        board.log_spiel("ERROR: You can't schrubb your own Schwein")
        return False
            
            
## @brief   discard_3 is the function for discarding 3 cards at once, which is only possible
#           if the player is not able to play any cards.
#
#  @param   game directory 
#
#  @details The function needs to check if NONE of the cards in the players hand can be played
#           For example: 
#           If a player has 3 "Blitzkarten" in his hand and no other player has
#           a "Stall" the player is allowed to discard all 3 cards and draw new ones.
#           
#           
#                     
#  @return  If all are fulfilled it returns a True statement else it returns a False
#           statement and the according ERROR message onto the board_log.     
    


def discard_3(game):
    spieler=game["dran_spieler"]
    
    anz_schweine = 7-game["anzahl_spieler"]
        
    anz = 0
    impossibility = 0
    
    
    card1 = ((((game["spielern"])[spieler])["aktion_karten"])["karten"])[0]
    card2 = ((((game["spielern"])[spieler])["aktion_karten"])["karten"])[1]
    card3 = ((((game["spielern"])[spieler])["aktion_karten"])["karten"])[2]
    
    cards = [card1, card2, card3]
    
    for card_number in range(3):
    
        if cards[card_number] == "Stallkarten":
            anz = 0
            for i in range(anz_schweine):
                if "Stallkarten" not in (((game["spielern"])[spieler])["schwein_karten"])[i]:
                    anz +=1
            
            if anz == 0:
                impossibility +=1
        
        
        
        if cards[card_number] == "Blitzableiterkarten":
            anz = 0
            for i in range(anz_schweine):
                if not("Blitzableiterkarten" in (((game["spielern"])[spieler])["schwein_karten"])[i]) and not ("Blitzableiterkarten-gold" in (((game["spielern"])[spieler])["schwein_karten"])[i]):
                    if "Stallkarten" in (((game["spielern"])[spieler])["schwein_karten"])[i]:
                        anz +=1
                    
            if anz == 0:
                impossibility +=1
                
        
        
        if cards[card_number] == "Blitzableiterkarten-gold":
            anz = 0
            for i in range(anz_schweine):
                if not ("Blitzableiterkarten" in (((game["spielern"])[spieler])["schwein_karten"])[i]) and not ("Blitzableiterkarten-gold" in (((game["spielern"])[spieler])["schwein_karten"])[i]):
                    if "Stallkarten" in (((game["spielern"])[spieler])["schwein_karten"])[i]:
                        anz +=1
                    
            if anz == 0:
                impossibility +=1
                
        
        
        
        if cards[card_number] == "Bauer-ärgere-dich-Karten":
            anz = 0
            for i in range(anz_schweine):
                if "Bauer-ärgere-dich-Karten" not in (((game["spielern"])[spieler])["schwein_karten"])[i]:
                    if "Stallkarten" in (((game["spielern"])[spieler])["schwein_karten"])[i]:
                        anz +=1
            
            if anz == 0:
                impossibility +=1
                
          
                
          
        if cards[card_number] == "Blitzkarten":
            anz = 0
            for ziel_spieler in range(game["anzahl_spieler"]):
                if ziel_spieler != spieler:
                    for i in range(anz_schweine):
                        if "Stallkarten" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[i]:
                            anz +=1
                    
            if anz == 0:
                impossibility +=1
                
        
        
        if cards[card_number] == "Bauer-schrubbt-die-Sau-Karten":
            anz = 0
            for ziel_spieler in range(game["anzahl_spieler"]):
                if ziel_spieler != spieler:
                    for i in range(anz_schweine):
                        if "Dreckschwein" in (((game["spielern"])[ziel_spieler])["schwein_karten"])[i] and "Bauer-ärgere-dich-Karten" not in (((game["spielern"])[ziel_spieler])["schwein_karten"])[i]:
                            anz +=1
                    
            if anz == 0:
                impossibility +=1
            
        
        
    
    
    if impossibility == 3:
    
        for i in range(3):
            (game["ablage_staple"]).append(((((game["spielern"])[spieler])["aktion_karten"])["karten"])[i])
        (((game["spielern"])[spieler])["aktion_karten"])["karten"].clear()
        for i in range(3):
            game=aux_functions.is_nachzieh_staple_full(game)
            (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
        return True

    else:
        board.log_spiel("YOU CAN PLAY A CARD")
        return False
                        
                        
                    

                
        
## @brief   discard_1 is the function for discarding one card which is always allowed.
#           
#  @param   karte Index of card which should be discarded
#  @param   game directory 
#
#  @details The player can choose to discard one card and draw a new one. This is always possible,
#           after drawing a card the players turn is over.
#                             
#  @return  None
#
            
                      
        
def discard_1(karte,game):
    spieler=game["dran_spieler"]
    (game["ablage_staple"]).append(karte)
    (((game["spielern"])[spieler])["aktion_karten"])["karten"].remove(karte)
    game=aux_functions.is_nachzieh_staple_full(game)
    (((game["spielern"])[spieler])["aktion_karten"])["karten"].append((game["nachzieh_staple"]).pop())
    

## @brief   reveal is the function for revealing the cards for the current player.
#           
#
#  @param   game directory 
#
#  @details The current player needs to have his cards revealed to know which cards he
#           can play. After every turn the cards need to be hidden again and the cards
#           of the next player need to revealed
#                             
#  @return  None
#


def reveal(game):
    spieler=game["dran_spieler"]
    leng = 3
    offset = game["anzahl_spieler"]-1
    
    if spieler !=0:
        ((((game["spielern"])[spieler])["aktion_karten"])["hidden"]).clear()
        ((((game["spielern"])[spieler-1])["aktion_karten"])["hidden"]).clear()
        for i in range(leng):
            ((((game["spielern"])[spieler-1])["aktion_karten"])["hidden"]).append(True)
            ((((game["spielern"])[spieler])["aktion_karten"])["hidden"]).append(False)
        board.draw_board(game)
    else:
        ((((game["spielern"])[spieler])["aktion_karten"])["hidden"]).clear()
        ((((game["spielern"])[spieler+offset])["aktion_karten"])["hidden"]).clear()
        for i in range(leng):
            ((((game["spielern"])[spieler+offset])["aktion_karten"])["hidden"]).append(True)
            ((((game["spielern"])[spieler])["aktion_karten"])["hidden"]).append(False)
        board.draw_board(game)
        




## @brief   win_condition is the function for checking if a player has won.
#           
#
#  @param   game directory 
#
#  @details For winning a game of Dreckschwein one player needs to have all his "Sauberschweine"
#           turned into "Dreckschweine".
#           After every turn it needs to be checked if the turn before the player made a winning move
#                             
#  @return  False if there was no winner last turn
#


def win_condition(game):
    if game["dran_spieler"] == 0:
        spieler = game["anzahl_spieler"]-1
        
        
    else:
        spieler = game["dran_spieler"]-1
    
    anz_schweine = 7-game["anzahl_spieler"]
    win_schweine = 0
    winner = 0
    
    #checks for how many Dreckschweine the player has
    for schwein_nr in range(anz_schweine):
        if "Dreckschwein" in (((game["spielern"])[spieler])["schwein_karten"])[schwein_nr]:
            win_schweine +=1
            
    
    if win_schweine == anz_schweine:
        winner = spieler
        return winner
    else:
        return False
            
## @brief   step is the whole loop of players taking their turn.
#           
#
#  @param   game directory 
#
#  @details The loop consits of a simple question and answer sequence. The user is can only
#           input "correct" inputs, meaning if there is a typo or a non allowed character
#           being input the user is put back to the first question.
#                             
#  @return  winner returns the player who has won the game
#
      
    

def step(game):
    runde = 0
    winner = -1
    while(True):
        if winner !=-1:
            return winner
            break
        else:
            
            runde +=1
            game["dran_spieler"]=0
        

 
        while game["dran_spieler"] < game["anzahl_spieler"] and winner == -1:
            if win_condition(game) != False:
                winner = win_condition(game)
                break
            
            
            spieler=game["dran_spieler"]
            handkarten = (((game["spielern"])[spieler])["aktion_karten"])["karten"]
            
            reveal(game)
            q1=board.input_ask(game,"Wollen Sie eine Karte Spielen? y/n-->  ")
            
            if q1 == "y":
                    
                q2 = board.input_ask(game,"Welche Karte wollen Sie spielen [0-2]-->  ")
                if q2.isdigit()== True:
                    q2 = int(q2)
                    if q2 <=2:
                        
                        q2=((((game["spielern"])[spieler])["aktion_karten"])["karten"])[q2]
                
                if q2 == "Matschkarten" and "Matschkarten" in handkarten:
                    schwein_nr = board.input_ask(game,"Welches Schwein wollen Sie zur Drecksau machen?-->  ")
                    
                    if schwein_nr.isdigit() == True:
                        schwein_nr = int(schwein_nr)
    
                        if  dreckschwein(schwein_nr,game) == True:
                        
                            board.log_spiel("Spieler "+str(spieler)+" macht seine Sau "+str(schwein_nr)+" dreckig")
                            game["dran_spieler"] +=1
                
                elif q2 == "Regenkarten":
                    
                    regenkarte(game)
                    game["dran_spieler"]+=1
                    
                elif q2 == "Stallkarten" and "Stallkarten" in handkarten:
                    schwein_nr = board.input_ask(game,"Welchem Schwein wollen Sie ein Stall bauen?-->  ")
                    
                    if schwein_nr.isdigit() == True:
                        schwein_nr = int(schwein_nr)
                    
                        if stallkarte(schwein_nr, game) == True:
                        
                            board.log_spiel("Spieler "+str(spieler)+" baut einen Stall auf Schwein "+str(schwein_nr)+ "")
                            game["dran_spieler"]+=1
                    
                elif q2 == "Blitzkarten" and "Blitzkarten" in handkarten:
                    ziel_spieler = board.input_ask(game,"Welchen Spieler wollen Sie angreifen?-->  ")
                    schwein_nr = board.input_ask(game,"Welches Schwein wollen Sie blitzen?-->  ")
                    
                    if schwein_nr.isdigit() == True and ziel_spieler.isdigit() == True:
                        ziel_spieler = int(ziel_spieler)
                        schwein_nr = int(schwein_nr)
                        
                    

                        if blitzkarte(schwein_nr,ziel_spieler,game) == True:
                       
                            board.log_spiel("Spieler "+str(spieler)+"  blitzt Stall von Spieler "+str(ziel_spieler)+ "")
                            game["dran_spieler"]+=1
                    
                elif q2 == "Blitzableiterkarten" and "Blitzableiterkarten" in handkarten: 
                    schwein_nr = board.input_ask(game,"Welchem Stall wollen Sie einen Blitzableiter bauen?-->  ")
                    
                    if schwein_nr.isdigit() == True:
                        schwein_nr = int(schwein_nr)
                        if blitzableiter(schwein_nr,game) == True:
                        
                            board.log_spiel("Spieler "+str(spieler)+"  baut Blitzableiter auf Schweinestall "+str(schwein_nr)+ "")
                            game["dran_spieler"]+=1

                elif q2 == "Blitzableiterkarten-gold" and "Blitzableiterkarten-gold" in handkarten: 
                    schwein_nr = board.input_ask(game,"Welchem Stall wollen Sie einen Blitzableiter bauen?-->  ")
                    
                    if schwein_nr.isdigit() == True:
                        schwein_nr = int(schwein_nr)
                        if blitzableiter_gold(schwein_nr,game) == True:
                        
                            board.log_spiel("Spieler "+str(spieler)+"  baut gold Blitzableiter auf Schweinestall "+str(schwein_nr)+ "")
                            board.log_spiel("Spieler "+str(spieler)+" can play again!")
                            
                    
                elif q2 == "Bauer-schrubbt-die-Sau-Karten" and "Bauer-schrubbt-die-Sau-Karten" in handkarten:
                    ziel_spieler = board.input_ask(game,"Welchen Spieler wollen Sie angreifen?-->  ")
                    schwein_nr = board.input_ask(game,"Welches Schwein wollen Sie sauber schrubben?-->  ")
                    
                    if schwein_nr.isdigit() == True and ziel_spieler.isdigit() == True:
                        ziel_spieler = int(ziel_spieler)
                        schwein_nr = int(schwein_nr)
                    
                        if bauerschrubb(schwein_nr,ziel_spieler,game) == True:
                        
                            board.log_spiel("Spieler "+str(spieler)+" schrubbt Schwein "+str(schwein_nr)+ " von Spieler "+str(ziel_spieler)+" sauber")
                            game["dran_spieler"]+=1
                    
                elif q2 == "Bauer-ärgere-dich-Karten" and "Bauer-ärgere-dich-Karten" in handkarten:
                    schwein_nr = board.input_ask(game,"Welchen Stall wollen Sie vernageln?-->  ")

                    if schwein_nr.isdigit() == True:
                        schwein_nr = int(schwein_nr)                    
                    
                        if baueraerger(schwein_nr,game) == True:
                       
                            board.log_spiel("Spieler "+str(spieler)+"  nagelt Schweinestall "+str(schwein_nr)+ " zu")
                            game["dran_spieler"]+=1
                else:
                    board.log_spiel("PLEASE TRY AGAIN WRONG INPUT")
                    
                

            
            elif q1 == "n":
                q2 = board.input_ask(game,"Wollen Sie eine einzelne Karte ablegen? (y/n)-->  ")
                if q2 == "y":
                    karte = board.input_ask(game,"Welche Karte wollen Sie ablegen-->  ")
                    if karte.isdigit() == True:
                        karte = int(karte)                        
                        
                        if karte <= 2:
                            karte= ((((game["spielern"])[spieler])["aktion_karten"])["karten"])[int(karte)]
                            discard_1(karte,game)
                            board.log_spiel("Spieler " +str(spieler)+ " legt "  +str(karte)+ " ab")
                            game["dran_spieler"]+=1

                
                if q2 == "n":
                    q3 = board.input_ask(game,"Wollen Sie alle 3 Karten ablegen? (y/n)-->  ")
                    
                    
                    if q3 == "y":
                        if discard_3(game) == True:
                            board.log_spiel("Spieler " +str(spieler)+ " legt alle 3 Karten ab")
                            game["dran_spieler"]+=1
                            
                            
                            
                    
            else:
                board.log_spiel("PLEASE TRY AGAIN WRONG INPUT")
                
                    
    