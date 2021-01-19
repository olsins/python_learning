# 1. Prototyp
# Nillas Abendteuer

#Startvariablen
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

