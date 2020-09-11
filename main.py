import random

liste = []

i = 0
while i < 6:
    zufallszahl = (random.randint(1,49))
    if zufallszahl not in liste:
        liste.append(zufallszahl)
        i += 1
liste.sort()
print(liste)
