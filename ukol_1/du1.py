# sloučení výpočtu Marinova, Lambertova a Braunova zobrazení
# volitelný poloměr Země a měřítko
# ošetření chybových hlášek při překročení vzdálenosti 1 m mezi přímkami sítě souřadnic

z = input("Zadej zobrazení:")
r = float(input("Zadej poloměr Země v km (s desetinnou tečkou):"))
m = int(input("Zadej měřítko (z tvaru 1:m zadej pouze číslo m):"))
u = int() # u je zeměpisná šířka
y = float()
v = int() # v je zeměpisná délka
x = float()

while z != "x":
    if z == "A":
        seznam_rovnobezky = []
        from math import pi
        for u in range(-90, 100, 10):
            y = (round(((r * (((u * 2) / 360) * pi) / m) * 100000), 1))
            # vynásobeno 100000 pro převod na cm a zaokrouhleno na 1 des. místo
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        seznam_poledniky = []
        for v in range(-180, 190, 10):
            x = (round(((r * (((v * 2) / 360) * pi) / m) * 100000), 1))
            if x <= -100.0 or x >= 100.0:
                seznam_poledniky.append("-")
            else:
                seznam_poledniky.append(x)
        break
    if z == "L":
        seznam_rovnobezky = []
        from math import pi, sin
        for u in range(-90, 100, 10):
            y = (round(((r * (sin((u * 2) / 360)) / m) * 100000), 1))
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        seznam_poledniky = []
        for v in range(-180, 190, 10):
            x = (round(((r * (((v * 2) / 360) * pi) / m) * 100000), 1))
            if x <= -100.0 or x >= 100.0:
                seznam_poledniky.append("-")
            else:
                seznam_poledniky.append(x)
        break
    if z == "B":
        seznam_rovnobezky = []
        from math import pi, tan
        for u in range(-80, 90, 10):  # fce tan není definována v 90°
            y = (round(((r * (tan((((u * 2) / 360) * pi) / 2)) / m) * 100000), 1))
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        seznam_poledniky = []
        for v in range(-180, 190, 10):
            x = (round(((r * (((v * 2) / 360) * pi) / m) * 100000),1))
            if x <= -100.0 or x >= 100.0:
                seznam_poledniky.append("-")
            else:
                seznam_poledniky.append(x)
        break
print("Zadané zobrazení:", z)
print("Zadaný poloměr Země je:", r, "km")
print("Zadané měřítko je: 1 :", m)
print("Rovnoběžky:", seznam_rovnobezky)
print("Poledníky:", seznam_poledniky)
