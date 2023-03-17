import math as m

def need():
    n = int(input("Fassungsvermögen pro Fass in l: "))
    order = int(input("BBestellte Menge "))
    count = m.ceil(order / n)
    print("Man braucht", count, "Fässer.")
need()
