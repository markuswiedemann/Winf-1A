Einkauf_Creme_Inhalt = 1000
Einkauf_Creme_Preis = 112
Verkauf_Creme_Inhalt = 50
Verkauf_Creme_Preis = 23.80
Fixkosten = 323000
Absatzmenge = 20000
Produktionsmenge = 20000

umsatz = Absatzmenge*Verkauf_Creme_Preis
print(umsatz)

Einkaufsmenge = (Verkauf_Creme_Inhalt*Absatzmenge)/Einkauf_Creme_Inhalt
print(Einkaufsmenge)