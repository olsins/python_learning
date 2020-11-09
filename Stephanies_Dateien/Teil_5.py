
# 5.1.1 Aufgabe
#animals = ["tiger", "mouse", "bird", "python", "elephant", "monkey"]

#for tier in animals:
   #print(tier + "ist ein Tier")

#5.1.2
#print("Bitte geben Sie fünf Worte ein!")
liste = []

#for i in range(0,5):
#    liste.append(input("Wort: "))
#print(liste)

#5.1.2.1
#anzahl = input("Wie viele Wörter wollen Sie eingeben?" )
#x = int(anzahl)
#for i in range(0, x):
#    liste.append(input("Wort: "))
#print(liste)

#Aufgabe 5.1.3
#n = input("Für welche Zahl soll die Fakultät berechnet werden?")
#x = int(n)+1
#liste = list(range(1, x))
#print(liste)
#liste.reverse()
#print(liste)
#ergebnis = x
#for i in range(1, x+1):
#    ergebnis = ergebnis * (liste[i])
#print(ergebnis)

antwort = input("Möchtest du Feierabend: ")

if antwort in ["Ja", "ja", "jep"]:
    print("Sehr gut!")
else:
    print("Ich glaube dir nicht!")