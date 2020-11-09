
# %%

# einfache liste // Array
liste = ['3', 'King Arthur', ['Rabbit', 3.4], 2.44]


liste = ['Schwalbe', 'Kokosnuss', 13, 'Spam', 3.14]
print(liste)

# len(liste) wie viele Elemente sind in der Liste
# liste.append('NI') - setze es hinten an die Liste ( bei ganzen Listen wird eine unterliste erstellt
# liste.extend([4,5,6,3.13]) --> Die erste Liste wird erweiter (kein Unterobjekt)
# liste.insert(2,'Taube') --> setze Taube auf zweiten Index (index 2 wird zu 3)
# liste.count(3.14) -> wie häufig ist das Objet drinn!
# liste.pop --> nimmt das letzte element raus

# %%


liste_a = ['Hallo', 'schönes', 'Wetter']
liste_b = liste_a
print(liste_a)
# Abgefahrene scheiße! durch liste_b = liste_a wird auch list_a zu liste_b
# %%
liste_b[1] = 'schlechtes'
print(liste_a)

liste_b = []
print(liste_a)


#print(liste_a[0], liste_a[1], liste_a[2])

# %%
a = 5
b = 6

b = a
b = 7
print(a)
print(b)
# %%
# Zusammenfassung: das ist völlig schrän
# bei arrays  a = b werden die irgendwie zusammengespeichert - aber nur das hinzufügen eines index ändert auch den index vom 2ten array
