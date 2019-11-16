# Výpočet Marinova, Lambertova, Braunova a Mercartorova zobrazení

from math import radians, pi, sin, tan, log

# ošetření chybového vstupu při zadávíní zobrazení
zobrazeni = input("Zadej počáteční písmeno zobrazení:")
while zobrazeni != "x":
    if zobrazeni == "A":
        zobrazeni = zobrazeni
        break
    elif zobrazeni == "B":
        zobrazeni = zobrazeni
        break
    elif zobrazeni == "L":
        zobrazeni = zobrazeni
        break
    elif zobrazeni == "L":
        zobrazeni = zobrazeni
        break
    else:
        print("Zadej správné počáteční písmeno zobrazení!")
        quit()

# volitelný poloměr Země
# pokud uživatel zadá 0, je poloměr roven 6371,11 km
# pokud zadá záporné číslo, program nahlásí chybu
polomer_km = float(input("Zadej poloměr Země v km (s desetinnou tečkou):"))
polomer_cm = polomer_km*100000
while polomer_cm != "x":
    if polomer_cm == 0:
        polomer_cm = 637111000
        break
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

zem_sirka = int()
y = float()
zem_delka = int()
x = float()
seznam_poledniky = []
seznam_rovnobezky = []

def vypocet_poledniky(zem_delka, polomer_cm, meritko):
    for zem_delka in range(-180, 190, 10): # výpočet poledníků je shodný pro všechna zobrazení
        x = (round((polomer_cm*(((zem_delka* 2)/360)*pi)/meritko),1))
        if x <= -100.0 or x >= 100.0:
            seznam_poledniky.append("-")
            # ošetření chybových hlášek při překročení vzdálenosti 1 m mezi přímkami sítě souřadnic
        else:
            seznam_poledniky.append(x)

def Marin_rovnobezky(zem_sirka, polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm*((radians(zem_sirka)))/meritko), 1)) # zaokrouhleno na 1 des. místo
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

def Lambert_rovnobezky(zem_sirka, polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm*(sin(radians(zem_sirka)))/meritko), 1))
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

def Braun_rovnobezky(zem_sirka, polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm * (tan(((radians(zem_sirka)))/2))/meritko), 1))
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

def Mercator_rovnoezky(zem_sirka, polomer_cm, meritko):
    for zem_sirka in range(-80, 90, 10):  # problém s 90°, proto jen do 80°
        y = (round((polomer_cm*(log(1/(tan(radians((90-zem_sirka)/2)))))/meritko), 1))
        if y <= -100.0 or y >= 100.0:
            seznam_rovnobezky.append("-")
        else:
            seznam_rovnobezky.append(y)

while zobrazeni != "x":
    if zobrazeni == "A":
        Marin_rovnobezky(zem_sirka, polomer_cm, meritko)
        vypocet_poledniky(zem_delka, polomer_cm, meritko)
        break
    elif zobrazeni == "L":
        Lambert_rovnobezky(zem_sirka, polomer_cm, meritko)
        vypocet_poledniky(zem_delka, polomer_cm, meritko)
        break
    elif zobrazeni == "B":
        Braun_rovnobezky(zem_sirka, polomer_cm, meritko)
        vypocet_poledniky(zem_delka, polomer_cm, meritko)
        break
    elif zobrazeni == "M":
        Mercator_rovnoezky(zem_sirka, polomer_cm, meritko)
        vypocet_poledniky(zem_delka, polomer_cm, meritko)
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