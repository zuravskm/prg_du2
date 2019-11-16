# Výpočet Marinova, Lambertova, Braunova a Mercartorova zobrazení

from math import radians, pi, sin, tan, log

zobrazeni = input("Zadej počáteční písmeno zobrazení:")

# volitelný poloměr Země
# pokud uživatel zadá 0, je poloměr roven 6371,11 km
# pokud zadá záporné číslo, program nahlásí chybu
polomer = float(input("Zadej poloměr Země v km (s desetinnou tečkou):"))
while polomer != "x":
    if polomer == 0:
        polomer = 6371.11
        break
    elif polomer < 0:
        print("Zadej správný poloměr Země!")
        break
    else:
        polomer = polomer
        break

# pokud uživatel zadá záporné měřítko, pogram nahlásí chybu
meritko = int(input("Zadej měřítko (z tvaru 1:m zadej pouze číslo m):"))
while meritko <= 0:
    print("Zadej správně měřítko!")
    break
zem_sirka = int()
y = float()
zem_delka = int()
x = float()
seznam_poledniky = []
seznam_rovnobezky = []

def vypocet_poledniky(zem_delka, polomer, meritko):
    for zem_delka in range(-180, 190, 10): # výpočet poledníků je shodný pro všechna zobrazení
        x = (round(((polomer*(((zem_delka* 2)/360)*pi)/meritko)*100000),1))
        if x <= -100.0 or x >= 100.0:
            seznam_poledniky.append("-")
            # ošetření chybových hlášek při překročení vzdálenosti 1 m mezi přímkami sítě souřadnic
        else:
            seznam_poledniky.append(x)

while zobrazeni != "x":
    if zobrazeni == "A":
        for zem_sirka in range(-90, 100, 10):
            y = (round(((polomer*((radians(zem_sirka)))/meritko)*100000), 1))
            # vynásobeno 100000 pro převod na cm a zaokrouhleno na 1 des. místo
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        vypocet_poledniky(zem_delka, polomer, meritko)
        break
    elif zobrazeni == "L":
        for zem_sirka in range(-90, 100, 10):
            y = (round(((polomer*(sin(radians(zem_sirka)))/meritko)*100000), 1))
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        vypocet_poledniky(zem_delka, polomer, meritko)
        break
    elif zobrazeni == "B":
        for zem_sirka in range(-90, 100, 10):
            y = (round(((polomer*(tan(((radians(zem_sirka)))/2))/meritko)*100000), 1))
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        vypocet_poledniky(zem_delka, polomer, meritko)
        break
    elif zobrazeni == "M":
        for zem_sirka in range(-80, 90, 10): # problém s 90°, proto jen do 80°
            y = (round(((polomer*(log(1/(tan(radians((90-zem_sirka)/2)))))/meritko)*100000), 1))
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        vypocet_poledniky(zem_delka, polomer, meritko)
        break
    else:
        print("Zadej správné počáteční písmeno zobrazení!")
        break

print("Zadané zobrazení:", zobrazeni)
print("Zadaný poloměr Země je:", polomer, "km")
print("Zadané měřítko je: 1 :", meritko)
print("Rovnoběžky:", seznam_rovnobezky)
print("Poledníky:", seznam_poledniky)