import random
import sys
import os

MojaZmienna = 0

while MojaZmienna < 25:
    MojaZmienna = MojaZmienna + 1
    if MojaZmienna == 20:
        print("Petla zaraz sie skonczy!")

print("Petla sie skonczyla poniewaz: MojaZmienna == ", MojaZmienna)


#Nastepna sekcja programu
#Czyli wykorzystywanie list

ListaDan = ["Sniadanie", "Obiad", "Kolacja", "Kupka"]
ListaNapojow = ["Kawa", "Herbata", "Sok"]

Licznik = 0

while Licznik < len(ListaDan):
    if Licznik == 0:
        ListaDan[Licznik] = ListaNapojow[Licznik+2]
        Licznik = Licznik + 1

    ListaDan[Licznik] = ListaDan[Licznik] + " " + ListaNapojow[Licznik-1]
    Licznik = Licznik + 1

Licznik = 0
while Licznik < len(ListaDan):
    print("Danie: ", ListaDan[Licznik])
    Licznik = Licznik + 1

print("Zakonczono!")

