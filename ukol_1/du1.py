# výpočet Marinova zobrazení pro volitelný poloměr Země a měřítko
# ošetření chybových hlášek při překročení vzdálenosti 1 m mezi přímkami sítě souřadnic
# sloučení výpočtu Marinova a Lambertova zobrazení

z = input("Zadej zobrazení:")
r = float(input("Zadej poloměr Země v km (s desetinnou tečkou):"))
m = int(input("Zadej měřítko (z tvaru 1:m zadej pouze číslo m):"))  # to je v cm
while z != "x":
    if z == "A":
        u = int() # u je zeměpisná šířka
        y = float()
        seznam_rovnobezky = []
        from math import pi
        for u in range(-90, 100, 10):
            y = (round(((r * (((u * 2) / 360) * pi) / m) * 100000), 1))
            # vynásobeno 100000 pro převod na cm a zaokrouhleno na 1 des. místo
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        v = int() # v je zeměpisná délka
        x = float()
        seznam_poledniky = []
        for v in range(-180, 190, 10):
            x = (round(((r * (((v * 2) / 360) * pi) / m) * 100000), 1))
            if x <= -100.0 or x >= 100.0:
                seznam_poledniky.append("-")
            else:
                seznam_poledniky.append(x)
        break
    if z == "L":
        u = int()
        y = float()
        seznam_rovnobezky = []
        from math import pi
        from math import sin
        for u in range(-90, 100, 10):
            y = (round(((r * (sin((u * 2) / 360)) / m) * 100000), 1))
            if y <= -100.0 or y >= 100.0:
                seznam_rovnobezky.append("-")
            else:
                seznam_rovnobezky.append(y)
        v = int()
        x = float()
        seznam_poledniky = []
        for v in range(-180, 190, 10):
            x = (round(((r * (((v * 2) / 360) * pi) / m) * 100000), 1))
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
