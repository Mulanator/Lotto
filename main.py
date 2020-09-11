import random

#Lösung mit Schleife
liste = []
i = 0
while i < 6:
    zufallszahl = (random.randint(1,49))
    if zufallszahl not in liste:
        liste.append(zufallszahl)
        i += 1
liste.sort()
print(liste)

#Alternative ohne Schleife
liste = []
zahlenraum = []
zahlenraum.extend(range(1, 49))
liste = random.sample(zahlenraum, 6)
liste.sort()
print(liste)
