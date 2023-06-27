# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 07:30:15 2021

@author: sayye
"""
import time
import random
import board
import sys



# =============================================================================
# =============================================================================
# # Drei Modes von Testing:
# #     MODE 1: test_mode=True and test_mode_2=False and test_mode_3=False
# #     Simuliert Spiel aber nach Spiel Ende wird gefragt, ob wir mit Simulation 
# #     weiter machen wollen.
# #     
# #     MODE 2: test_mode=True and test_mode_2=True  and test_mode_3=False
# #     Simuliert Spiel aber nach Spiel Ende wird nicht gefragt, ob wir mit Simulation 
# #     weiter machen wollen. Es simuliert unendlich mal. Die wahrscheinlichkeiten
# #     sind auch anders gewichtet-->siehe test_game_2() Funktion
# #     
# #     MODE 3: test_mode=True and test_mode_2=False  and test_mode_3=True
# #     Testet eine spezifische Reihenfolge von Nachziehkarten Staple und wenn es nicht 
# #     richtig raus kommt, wird es geloggt, dass der Test nicht bestanden ist
# =============================================================================
# =============================================================================
    
    







speed=0.001 # Geschwindigkeit von Simulation in sekunden
test_mode=False
test_mode_2=False
test_mode_3=False










## @brief sleep function. Das game wird pausiert für Anzahl sekunden in global speed
#         variable
#  @return None
def sleep():
    global speed
    time.sleep(speed)



## @brief getter funktion
#  @return test_mode
def is_test_mode():
    global test_mode
    return test_mode




#to keep the count of how many times test_game_2 function is entered
count_2=0

## @brief getter funktion
#  @return test_mode?2
def is_test_2_mode():
    return test_mode_2


## @brief Implementiert test_mode_3
#  @param game game dictionary
#  @param s Die Frage, die wir simulieren
#  @return game dictionary
def test_game_2(game,s=""):

    global count_2
    global test_mode_2
    sleep()
    if ( (((game["spielern"])[0])["aktion_karten"])["karten"] == ["Matschkarten","Matschkarten","Matschkarten"] ):
        if(s=="Wollen Sie eine Karte Spielen? y/n-->  "):
            if count_2==0:
                count_2+=1
                return "n" 

            elif count_2>=1:
                board.log_spiel("Sorry, der Test ist nicht bestanden!")
                sys.exit()
                return
            

        if (s=="Wollen Sie alle 3 Karten ablegen? (y/n)-->  "):
            return "y" 
        
        elif (s=="Wollen Sie eine einzelne Karte ablegen? (y/n)-->  "):
            return "n"
        else:
            return "n"
    else:
        #Mit normalen Simulation weiter machen, weil es unser Sequenz nicht entspricht
        test_mode_2=False
        return test_game
        
        
    

## @brief Implementiert test_mode_2. Antwort jede Frage zufällig aber 
#         aber unterschiedlich gewichtet, damit wir 3 Karten ablegen Kondition
#         in logic module besser testen können.
#  @param game game dictionary
#  @param s Die Frage, die wir simulieren
#  @return game dictionary
def test_game_3(game,s):
        n=game["anzahl_spieler"]
        sauberscheine=5
        if n==3:
            sauberscheine=4
        if n==4:
            sauberscheine=3
            
            
        aktion_karten=3
        sleep()
        if(s=="Wollen Sie eine Karte Spielen? y/n-->  "):
            willingness=random.choices(["y","n"],weights=(10,90))
            return willingness[0]    
    
        if (s=="Wollen Sie alle 3 Karten ablegen? (y/n)-->  "):
            willingness=random.choices(["y","n"],weights=(90,10))
            return willingness[0]          
            
        if(s=="Wollen Sie eine einzelne Karte ablegen? (y/n)-->  "):
            willingness=random.choices(["y","n"],weights=(10,90))
            return willingness[0]       
        
        if(s=="Welches Schwein wollen Sie zur Drecksau machen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness        
            
        if(s=="Welchem Schwein wollen Sie ein Stall bauen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness         
            
        if(s=="Welchen Spieler wollen Sie angreifen?-->  "):
            willingness=str(random.choice(range(n)))
            return willingness     
        
        if(s=="Welches Schwein wollen Sie blitzen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness 
            
        if(s=="Welchem Stall wollen Sie einen Blitzableiter bauen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness 
        
        if(s=="Welches Schwein wollen Sie sauber schrubben?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness 
        
        if(s=="Welchen Stall wollen Sie vernageln?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness    
    
        if(s== "Welche Karte wollen Sie spielen [0-2]-->  "):
            willingness=str(random.choice(range(aktion_karten)))
            return willingness    
        
        if(s=="Welche Karte wollen Sie ablegen-->  "):
            willingness=str(random.choice(range(aktion_karten)))
            return willingness    
    
        else:
            print("not_included_string_in_test")
            return    




## @brief Implementiert test_mode_2. Antwort jede Frage zufällig mit uniform Verteilung.
#  @param game game dictionary
#  @param s Die Frage, die wir simulieren
#  @return "y","n" oder eine Zahl, die die spezifische Frage antwortet.
def test_game(game,s=""):
    #if test_mode_2 is True
    #We change the game dictionary
    #and run the test_game_2 test instead of test_game
    if(test_mode_2):
        return test_game_2(game,s)
        
    if (test_mode_3):
        return test_game_3(game,s)
    else:
        n=game["anzahl_spieler"]
        sauberscheine=5
        if n==3:
            sauberscheine=4
        if n==4:
            sauberscheine=3
            
            
        aktion_karten=3
        sleep()
        if(s=="Wollen Sie eine Karte Spielen? y/n-->  "):
            willingness=random.choice(["y","n"])
            return willingness   
    
        if (s=="Wollen Sie alle 3 Karten ablegen? (y/n)-->  "):
            willingness=random.choice(["y","n"])
            return willingness          
            
        if(s=="Wollen Sie eine einzelne Karte ablegen? (y/n)-->  "):
            willingness=random.choice(["y","n"])
            return willingness      
        
        if(s=="Welches Schwein wollen Sie zur Drecksau machen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness        
            
        if(s=="Welchem Schwein wollen Sie ein Stall bauen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness         
            
        if(s=="Welchen Spieler wollen Sie angreifen?-->  "):
            willingness=str(random.choice(range(n)))
            return willingness     
        
        if(s=="Welches Schwein wollen Sie blitzen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness 
            
        if(s=="Welchem Stall wollen Sie einen Blitzableiter bauen?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness 
        
        if(s=="Welches Schwein wollen Sie sauber schrubben?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness 
        
        if(s=="Welchen Stall wollen Sie vernageln?-->  "):
            willingness=str(random.choice(range(sauberscheine)))
            return willingness    
    
        if(s== "Welche Karte wollen Sie spielen [0-2]-->  "):
            willingness=str(random.choice(range(aktion_karten)))
            return willingness    
        
        if(s=="Welche Karte wollen Sie ablegen-->  "):
            willingness=str(random.choice(range(aktion_karten)))
            return willingness    
    
        else:
            print("not_included_string_in_test")
            return