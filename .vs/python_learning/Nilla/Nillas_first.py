# 1. Prototyp
# Nillas Abendteuer

#Startvariablen

class room:
    def __init__(self, name, description,):
        self.name = name
        self.description = description
        self.exits = {}

#define all rooms:
berg = room("Berg",
    "Der höchste alle Berge war seit Jahrtausenden Heimat der Zwerg*innen. Auf seiner"
    "Spitze herrschten -100°C.")
wald = room("Wald", 
    "Im alten Wald ächzente die Bäume in Wind und das Sonnenlicht tanzte durch die Blätter.")
meer = room("Meer",
    "Das große, unendliche Meer in dessen Tiefen Ungeheuer, aber auch Abendteuer und"
    "neue Freundschaften warteten.")
wueste = room("Wüste",
    "Die Luft flimmerte in der Hitze, die Tagsüber in der Wüste herrschte und Nachts war"
    "die Kälte so schlimm, dass sich sogar Kakteen nach ein wenig Nähe und Wärme sehnten.")
gebirge = room("Gebirge",
    "Die großen Berge ragten wie Riesen (zwinker smiley) vor Dir auf.")
stadt = room("Stadt",
    "Die alte Stadt war einst ein Handelsknotenpunkt zwischen all den verschiedenen"
    "Landschaften und ihren Bewohner*innen gewesen und lag nun schon seit vielen Jahren"
    "in einem Zauberschlaf.")

# 4 Richtungsknöpfe
u = 'unten'
o = 'oben'
r = 'rechts'
l = 'links'


print('________________Nillas Abendteuer____________________________________')

print('Nilla ist eine abendteuerlustige Zwergin, die von ihren Mitzwerg*innen\n'
        'genervt war, die immer nur darauf aus waren, Gold zu finden.\n'
        'Eines schönen Tages entschloss sich Nilla den Berg zu verlassen\n'
        'und Neues kennenzulernen.')

print('Wohin möchtest du gehen? Für Wüste schreibe oben(o), für Wald rechts(r),\n'
        'für Meer unten(u) und für Gebirge links(l)!')
inputvariable = input()

if inputvariable == 'u':
    print(u)
elif inputvariable == 'o':
    print(o)
elif inputvariable == 'r':
    print(r)
elif inputvariable == 'l':
    print(l)

