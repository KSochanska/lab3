# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def nazwafunkcji():
    print ("wywołałes funckję, nazwa funkcji")
    print ("ciało funkcji")
    print ("koniec funkcji")

def funkcjazargumentem(zmienna):
    print ("podałes zmienną, która wynosi", zmienna)
    
def silnia(n):
    
   
    silnia = 1
    i = 1

    while i <= n:
        silnia = silnia * i
        i = i + 1
    print ('silnia = ', silnia)

nazwafunkcji()
nazwafunkcji()
funkcjazargumentem(5)
silnia(3)
silnia(1)
silnia(2)
    