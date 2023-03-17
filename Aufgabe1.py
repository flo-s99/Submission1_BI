# Eingabe beider Daten
l = float(input("Geben Sie die Länge des Rechtecks ein: "))
b = float(input("Geben Sie die Breite des Rechtecks ein: "))

# Umfang und Fläche
def umfang(l, b):
    umfang = 2 * (l + b)
    print("Umfang des Rechtecks:",umfang)
def flaeche(l,b):
    flaeche = l * b
    print("Fläche des Rechtecks:",flaeche)

umfang(l,b)
flaeche(l,b)
