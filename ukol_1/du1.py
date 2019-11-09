# výpočet Marinova zobrazení pro volitelný poloměr Země a měřítko

r = float(input("Zadej poloměr Země v km (s desetinnou tečkou):"))
m = int(input("Zadej měřítko (z tvaru 1:m zadej pouze číslo m):")) # to je v cm

print("Zadaný poloměr Země je:", r, "km")
print("Zadané měřítko je: 1:", m)

#v je zeměpisná délka
v = int()
x = float()
seznam_rovnobezky = []
from math import pi
for v in range(-90,100,10):
    x = (round(((r*(((v* 2)/360)*pi)/m)*100000),1)) #vynásobeno 100000 pro převod na cm a zaokrouhleno na 1 des. místo
    seznam_rovnobezky.append(x)
print("Rovnoběžky:", seznam_rovnobezky)

#u je zeměpisná šířka
u = int()
y = float()
seznam_poledniky = []
for u in range(-180,190,10):
    y = (round(((r*(((u*2)/360)*pi)/m)*100000), 1))
    seznam_poledniky.append(y)
print("Poledníky:", seznam_poledniky)