# Výpočet Marinova, Lambertova, Braunova a Mercartorova zobrazení

from math import radians, pi, sin, tan, log

# ošetření chybového vstupu při zadávíní zobrazení
# pokud uživatel zadá x program skončí
# pokud uživetel zadá jiné písmeno, program ho upozorní a skončí
zobrazeni = input("Zadej počáteční písmeno zobrazení:")
def kontrola_zobrazeni (zobrazeni):
    while zobrazeni != "0":
        if zobrazeni == "A":
            return zobrazeni
        elif zobrazeni == "B":
            return zobrazeni
        elif zobrazeni == "L":
            return zobrazeni
        elif zobrazeni == "M":
            return zobrazeni
        elif zobrazeni == "x":
            print("Zadal jsi x, program končí.")
            quit()
        else:
            print("Zadej správné počáteční písmeno zobrazení!")
            quit()
kontrola_zobrazeni(zobrazeni)

# volitelný poloměr Země
# pokud uživatel zadá 0, je poloměr roven 6371,11 km
# pokud zadá záporné číslo, program nahlásí chybu
# pokud uživatel zadá x, program skončí
polomer_km = float(input("Zadej poloměr Země v km (s desetinnou tečkou):"))
polomer_cm = polomer_km*100000
while polomer_cm != "I":
    if polomer_cm == 0:
        polomer_cm = 637111000
        break
    elif polomer_cm == "x":
        print("Zadal jsi x, program končí.")
        quit()
    elif polomer_cm < 0:
        print("Zadej správný poloměr Země!")
        quit()
    else:
        polomer_cm = polomer_cm
        break

# pokud uživatel zadá záporné měřítko, pogram nahlásí chybu
meritko = int(input("Zadej měřítko (z tvaru 1:m zadej pouze číslo m):"))
while meritko <= 0:
    print("Zadej správně měřítko!")
    quit()

zem_delka = int()
zem_sirka = int()
seznam_rovnobezky = []
seznam_poledniky = []

def vypocet_poledniky(polomer_cm, meritko):
    x = float()
    for zem_delka in range(-180, 190, 10): # výpočet poledníků je shodný pro všechna zobrazení
        x = (round((polomer_cm*(((zem_delka* 2)/360)*pi)/meritko),1))
        if x <= -100.0 or x >= 100.0:
            seznam_poledniky.append("-")
            # ošetření chybových hlášek při překročení vzdálenosti 1 m mezi přímkami sítě souřadnic
        else:
            seznam_poledniky.append(x)

def Marin_rovnobezky(polomer_cm, meritko):
    y = float()
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm*((radians(zem_sirka)))/meritko), 1)) # zaokrouhleno na 1 des. místo
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

def Lambert_rovnobezky(polomer_cm, meritko):
    y = float()
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm*(sin(radians(zem_sirka)))/meritko), 1))
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

def Braun_rovnobezky(polomer_cm, meritko):
    y = float()
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm * (tan(((radians(zem_sirka)))/2))/meritko), 1))
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

def Mercator_rovnobezky(polomer_cm, meritko):
    y = float()
    for zem_sirka in range(-80, 90, 10):  # problém s 90°, proto jen do 80°
        y = (round((polomer_cm*(log(1/(tan(radians((90-zem_sirka)/2)))))/meritko), 1))
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

while zobrazeni != "x":
    if zobrazeni == "A":
        Marin_rovnobezky(polomer_cm, meritko)
        vypocet_poledniky(polomer_cm, meritko)
        break
    elif zobrazeni == "L":
        Lambert_rovnobezky(polomer_cm, meritko)
        vypocet_poledniky(polomer_cm, meritko)
        break
    elif zobrazeni == "B":
        Braun_rovnobezky(polomer_cm, meritko)
        vypocet_poledniky(polomer_cm, meritko)
        break
    elif zobrazeni == "M":
        Mercator_rovnobezky(polomer_cm, meritko)
        vypocet_poledniky(polomer_cm, meritko)
        break

print("Zadané zobrazení:", zobrazeni)
while polomer_km != "x":
    if polomer_km == 0:
        print("Zadaný poloměr Země je: 6371.11 km")
        break
    else:
        print("Zadaný poloměr Země je:", polomer_km, "km")
        break
print("Zadané měřítko je: 1 :", meritko)
print("Rovnoběžky:", seznam_rovnobezky)
print("Poledníky:", seznam_poledniky)