# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:49:32 2021

@author: sayye
"""





## @brief initializiert game dictionary aber mit einer bestimmten Reihenfolge
#         von Karten, dass wir zum Test Zwecken brauchen.
#  @return Intialisierte Game dictionary
def init_spiel(n):
    #First Sequence:
    #zum testen, ob man 3 Karten ablegen kann. Drei Karten ablegen muss nicht 
    #möglich sein, weil die
    #ersten 3 Karten Matchkarten sind und am Anfang sind alle Schweine sauber
    all_cards=[21*["Matschkarten"], 4*["Regenkarten"], 9*["Stallkarten"], 4*["Blitzkarten"], 
            4*["Blitzableiterkarten"], 8*["Bauer-schrubbt-die-Sau-Karten"], 
            4*["Bauer-ärgere-dich-Karten"], 2*["Blitzableiterkarten-gold"]]
    karten=[]
    for i in range(len(all_cards)):
        for j in range(len(all_cards[i])):
            karten.append(all_cards[i][j])
     
    #inplace reverse the list because when we pop, then we have the first elment
    #of the list and not the last        
    karten.reverse()
    #default game: we have at least two players
    game={
    "dran_spieler":0,
    "anzahl_spieler":    2,
    "nachzieh_staple"   :    karten,
    "ablage_staple"     :    [],
    "spielern"          :    {
                              0:    {
                                      "aktion_karten":{
                                                      "karten":[karten.pop() for i in range(3)],
                                                      "hidden":[True,True,True]
                                                      },
                                      "schwein_karten"   :{
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"],
                                                          3:["Sauberschwein"],
                                                          4:["Sauberschwein"]
                                                     }       
                                    },
                              1:    {
                                      "aktion_karten":{
                                                      "karten":[karten.pop() for i in range(3)],
                                                      "hidden":[True,True,True]
                                                      },
                                      "schwein_karten"   :{
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"],
                                                          3:["Sauberschwein"],
                                                          4:["Sauberschwein"]                                                          
                                                     }       
                                     }
                              
                             }
        }

    
    if n==3:
        game["anzahl_spieler"]=3
        ((game["spielern"])[0])["schwein_karten"]=    {
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"],
                                                          3:["Sauberschwein"]
                                                     }
        ((game["spielern"])[1])["schwein_karten"]=    {
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"],
                                                          3:["Sauberschwein"]
                                                     }
              
                                     
        (game["spielern"])[2]=    {
                                      "aktion_karten":{
                                                      "karten":[karten.pop() for i in range(3)],
                                                      "hidden":[True,True,True]
                                                      },
                                      "schwein_karten"   :{
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"],
                                                          3:["Sauberschwein"]
                                                     }       
                                     }
    if n==4:
        game["anzahl_spieler"]=4
        ((game["spielern"])[0])["schwein_karten"]=   {
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"]

                                                     }
        ((game["spielern"])[1])["schwein_karten"]=   {
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"]

                                                     }
        
        (game["spielern"])[2]=   {
                                      "aktion_karten":{
                                                      "karten":[karten.pop() for i in range(3)],
                                                      "hidden":[True,True,True]
                                                      },
                                      "schwein_karten"   :{
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"]

                                                          }       
                                 }
                              
                             
              
                                     
        (game["spielern"])[3]=    {
                                      "aktion_karten":{
                                                      "karten":[karten.pop() for i in range(3)],
                                                      "hidden":[True,True,True]
                                                      },
                                      "schwein_karten"   :{
                                                          0:["Sauberschwein"],
                                                          1:["Sauberschwein"],
                                                          2:["Sauberschwein"]

                                                          }       
                                     }
    return game
