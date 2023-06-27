# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:11:03 2021

@author: sayye
"""
from __future__ import print_function
import colorama
from colorama import Fore, Back, Style, Cursor
from random import randint, choice
from string import printable
import os
import sys
from testing import test_the_whole_game







# Alle Karten Arten als Charakterkette
card_type=["Sauberschwein","Drecksau","Matschkarten", "Regenkarten","Stallkarten","Blitzkarten", 
        "Blitzableiterkarten", "Blitzableiterkarten-gold","Bauer-schrubbt-die-Sau-Karten", 
        "Bauer-ärgere-dich-Karten","Leer","Unbekannt"]

# Alle Foreground, Background und Style Optionen innerhalb Colorama Bibliothek als
# 3 Listen. Die drei listen vereinfachen den Zugang.
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]


# Am besten 1920*1080 Auflosung und mit 100% Skalierung
# Die Variabeln da sind frame Grössen
MINY, MAXY = 2, 45
MINX, MAXX = 4, 160
RANGEX=MAXX-MINX
RANGEY=MAXY-MINY
MinFrameY, MaxFrameY=MINY+3,MAXY-2
MinFrameX,MaxFrameX=MINX+2,MAXX-2
RangeFrameY=MaxFrameY-MinFrameY
RangeFrameX=MaxFrameX-MinFrameX
MinLogY,MinLogX=MINY+2,MAXX+3

colorama.init()

 
log_liste=[]    


## @brief Fragt den Nutzer, die Anzahl von Spielern. 
#  @details Nutzer kann zwischen 2,3,4  wählen.  

#  @return returns anzahl spieler im Spiel
def nspieler():
    while True:
        # put cursor to top, left, and set color to white-on-black with normal brightness.
        print('%s%s%s%s' % (pos(MAXY+2, MINX), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
        nSpieler=int(input("Wie Viele Spieler? [2,3 oder 4] ---->  "))
        
        if (2<=nSpieler<=4):
            print ('%s%s' % (pos(MAXY+2, MINX)," "*RANGEX))
            print('%s%s%s%s' % (pos(MAXY+2, MINX), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
            return nSpieler
        
        print ('%s%s' % (pos(MAXY+2, MINX)," "*RANGEX))
        continue 









## @brief clears the console
#  @return None

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')#clears the console
    


## @brief returns position of the Cursor
#  @param y coordinate y
#  @param x coordinate x
#  @return returns position of the Cursor
def pos(y,x):
    return Cursor.POS(x, y)


## @brief macht ein Spiel Board mit Rahmen, aber ohne Karten.
#  @details Die Funktion wird gebraucht, um das Board zu initialisieren 
#  @return None
def white_board():
    clearConsole()

    print(Back.CYAN, end='')
    print('%s%s' % (pos(MINY, MINX), ' '*RANGEX), end='')
    for y in range(MINY, 1+MAXY):
        print('%s %s ' % (pos(y, MINX), pos(y, MAXX)), end='')
    print('%s%s' % (pos(MAXY, MINX), ' '*RANGEX), end='')
    
 
    
 
    
 
## @brief Wrapped den Namen von Karte in einer Breite von b 
#  @param card_name Der Name von Karte
#  @param b Die Breite von Karte
#  @coordinate coordinate Tuple, die die Koordinaten von top left von Karte ist
#  @return None
def WRAP(card_name,b,coordinate):
    y,x=coordinate
    count=0
    for i in range(0,len(card_name)+1,b):
        rest=card_name[i:i+b]
        if len(rest)==b:
            print('%s' % (pos(y+count, x)),end="")
            print("{:<8}".format(rest),end="")
            count+=1
        else:
            print('%s' % (pos(y+count, x)),end="")
            print("{:<8}".format(rest),end="")
            count+=1
            
    #The following loop makes sure that every card has 3 lines
    while count<4:
        print('%s' % (pos(y+count, x)),end="")
        print("{:<8}".format(" "),end="")
        count+=1        
        
  
    



## @brief Zeichnet die Karte auf dem Schirm
#  @param card_name Der Name von Karte
#  @param b Die Breite von Karte
#  @param coordinate Tuple, die die Koordinaten von top left von Karte ist
#  @return None
def draw_card(card_name,b,coordinate):
    #All the font colors are bright
    print(Style.BRIGHT,end="")
    
    if card_name == "Sauberschwein":
        print(Back.MAGENTA,end="")
        print(Fore.WHITE,end="")
        
    elif card_name =="Drecksau":
        print(Back.LIGHTGREEN_EX,end="")
        print(Fore.WHITE,end="")        
            
    elif card_name =="Blitzkarten":
        print(Back.RED,end="")
        print(Fore.WHITE,end="")
        
    elif card_name =="Blitzableiterkarten":
        print(Back.GREEN,end="")
        print(Fore.WHITE,end="")
            
    elif card_name =="Matschkarten":
        print(Back.YELLOW,end="")
        print(Fore.BLACK,end="")
        
    elif card_name =="Regenkarten":
        print(Back.MAGENTA,end="")
        print(Fore.WHITE,end="")
        
    elif card_name =="Stallkarten":
        print(Back.GREEN,end="")
        print(Fore.WHITE,end="")

    elif card_name =="Bauer-ärgere-dich-Karten":
        print(Back.GREEN,end="")
        print(Fore.WHITE,end="")
        
    elif card_name =="Blitzableiterkarten-gold":
        print(Back.GREEN,end="")
        print(Fore.WHITE,end="")
           
        
    elif card_name=="Bauer-schrubbt-die-Sau-Karten":
        print(Back.RED,end="")
        print(Fore.WHITE,end="")
        
    elif card_name == "empty" :
        print(Style.NORMAL,end="")
        print(Fore.BLACK)
        print(Back.WHITE,end="")
    else:
        print(Fore.BLACK)
        print(Back.WHITE,end="")


    WRAP(card_name, b,coordinate)

    
 
    
## @brief Zeichnet den Pfeil, was den Spieler zeigt, der dran ist.
#  @param y y Koordinate   
#  @param x x Koordinate 
#  @return None
def draw_pfeil (y,x):
    print(Back.BLACK, end='')
    print(Fore.CYAN, end='')  
    print('%s%s' % (pos(y, x),"/\\"), end='')
    print('%s%s' % (pos(y+1, x),"||"), end='')
    print('%s%s' % (pos(y+2, x),"\\/"), end='')        
 
    
## @brief Das ist interface zwischen board.py und logic.py
#         Es gibt an Spieler weiter, was logic Module verlangt und 
#         gibt das Input von Spieler an logic Module zurück.  
#  @param game das Dictionary von init.py
#  @param s s wird angezeigt, bevor der Spieler etwas eingibt.
#  @return input von Spieler
def input_ask (game,s=""):
    # put cursor to bottom, left, and set color to white-on-black with normal brightness.
    print('%s%s%s%s' % (pos(MAXY+2, MINX), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
    generic_input=""
    #If the test_mode variable in test_the_whole_game is set
    #we don't ask the user for an input
    if test_the_whole_game.is_test_mode():
        generic_input=test_the_whole_game.test_game(game,s)
    else:
        generic_input=input(s)
        
    print ('%s%s' % (pos(MAXY+2, MINX)," "*RANGEX))
    print('%s%s%s%s' % (pos(MAXY+2, MINX), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
    return generic_input
    
     












## @brief Wrapped den Log in einer Breite von b 
#  @param b Die Breite von log
#  @param coordinate coordinate Tuple, die die Koordinaten von top left von log ist
#  @return None
def wrap_log(b,coordinate):
    print(Back.BLACK, end='')
    print(Style.BRIGHT, end='') 
    print(Fore.RED, end='') 
    y,x=coordinate
    count=0
    last_logs=log_liste[-10:]
    for log_string in last_logs:
        for i in range(0,len(log_string)+1,b):
            rest=log_string[i:i+b]
            if len(rest)==b:
                print('%s' % (pos(y+count, x)),end="")
                print("{:<30}".format(rest),end="")
                count+=1
            else:
                print('%s' % (pos(y+count, x)),end="")
                print("{:<30}".format(rest),end="")
                count+=1
                
        #The following loop makes sure that every card has 3 lines
        while count<4:
            print('%s' % (pos(y+count, x)),end="")
            print("{:30}".format(" "),end="")
            count+=1 
            
            
            
## @brief appended das Parameter s an log Liste  
#  @param s string, wo apppeded wird an Log Liste
#  @return None        
def log_spiel (s=""):
    log_liste.append(s)
    wrap_log(30, (MinLogY,MinLogX))
    return
 
    
 
## @brief Zeichnet die Nummer von jeder Karte unten auf dem Spiel board.
#  @param y y Koordinate   
#  @param x x Koordinate 
#  @return None  
def draw_card_Nr (i,y,x):
    print(Back.BLACK, end='')
    print(Fore.WHITE, end='')  
    print('%s' % (pos(y, x)), end='')
    print(i)
 
    
 
    
 
## @brief Zeichnet den Staple auf jedem Schwein.
#  @param game Das ist das Game dictionary 
#  @param y y Koordinate   
#  @param x x Koordinate 
#  @return None 
def draw_staple (game,y,x):
    print(Back.BLUE, end='')
    print(Fore.CYAN, end='')  
    print('%s' % (pos(y-1, x-30)), end='')
    print("{:<18}".format("# Nachzieh_Karten"),end="")
    print('%s' % (pos(y-1, x-10)), end='')   
    print("{:<18}".format("# Ablage_Karten"),end="")
    print('%s' % (pos(y, x-30)), end='')
    print("     ","{:<12}".format(len(game["nachzieh_staple"])),end="")
    print('%s' % (pos(y, x-10)), end='')
    print("     ","{:<12}".format(len(game["ablage_staple"])),end="")

## @brief Zeichnet die Nummer von jedem Spieler unten auf dem Spiel board.
#  @param y y Koordinate   
#  @param x x Koordinate 
#  @return None 
def draw_spieler_Nr (spieler,y,x):   
    print(Back.BLACK, end='')
    print(Fore.YELLOW, end='')  
    print('%s' % (pos(y, x)), end='')
    print("Spieler-",spieler,sep="") 
    
## @brief Interface zwischen logic und board. Es wird ein Board gezeichnet
#         basiert auf dem Game dictionary  
#  @param game Das Game dictionary
#  @return None
def draw_board(game):
    spieler=game["dran_spieler"]
    white_board()
    n=game["anzahl_spieler"]
    #integer division:
    breite=RangeFrameX//n
    pfeil_pos_y=MinFrameY+7
    draw_staple(game,MaxFrameY-23, MinFrameY+RangeFrameX//2)
    b=8
    for i in range(n):
        x_down=MinFrameX+i*breite
        y_down=MaxFrameY-4
        
        #Draw Schweinekarten
        sauberscheine=5
        if n==3:
            sauberscheine=4
        if n==4:
            sauberscheine=3
   
        for j in range(sauberscheine):
            for h in range(len( (((game["spielern"])[i])["schwein_karten"])[j] )):
                draw_card(((((game["spielern"])[i])["schwein_karten"])[j])[h], b, (y_down-5*h,x_down))
            draw_card_Nr(j, y_down+4, x_down+5)
            x_down+=10
        

        #Draw Aktionskarten
        x_up=MinFrameX+i*breite
        y_up=MinFrameY        
        #Anzahl action cards is always 3
        for h in range(len( (((game["spielern"])[i])["aktion_karten"])["karten"] )):
            if ( ((((game["spielern"])[i])["aktion_karten"])["hidden"])[h] ):
                draw_card("unbekannt", b, (y_up,x_up))
            else:
                draw_card_Nr(h, y_up+5, x_up+5)
                draw_card(   ((((game["spielern"])[i])["aktion_karten"])["karten"])[h]  , b, (y_up,x_up))                
            x_up+=10
            
            
        
        #Draw pfeil
        pfeil_pos_x=MinFrameX+i*breite+breite//4
        if i==spieler:
            draw_pfeil(pfeil_pos_y,pfeil_pos_x)
        
        #Draw Spieler Nr.
        draw_spieler_Nr(i,y_down+5 ,pfeil_pos_x)
    log_spiel()    
    return 
        
    

