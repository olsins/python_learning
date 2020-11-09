# Schreibe ein Programm, welches
# die Länge der Diagonale eines Rechtecks
# mit den Seitenlängen a und b berechnet.
from math import sqrt

# %%
a = float(input("Gibt ein Wert für die Seitenlänge a ein"))
b = float(input("Gibt einen Wert für die Seitenlägen b ein"))
c = a * a + b * b
c = sqrt(c)
print("die diagonole ist", c)

# %%
