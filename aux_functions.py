# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 06:40:59 2021

@author: sayye
"""

import random



## @brief Die Funktion checked, ob nachzieh_staple leer ist.
#         Wenn ja, dann wird nazhieh_staple gleich ablage_staple gesetzt und geschuffelt.        
#  @return game dictionary  
def is_nachzieh_staple_full (game):
        nachzieh=game["nachzieh_staple"]
        ablage=game["ablage_staple"]
        if(len(nachzieh)<=0):
            random.shuffle(ablage)
            game["nachzieh_staple"]=ablage
            game["ablage_staple"]=[]
        return game