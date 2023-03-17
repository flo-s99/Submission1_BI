# eingabe von n
n = int(input("Geben Sie n ein: "))



# Funktion zum Summieren
def sum(n):
    # Ausgangssumme
    sum = 0
    # Durch jedes i in der range n iterieren
    for i in range(1, n+1):
        # Summe immer um 1 erhöhen
        sum += i
        print("Die Summe der Zahlen von 1 bis", n, "ist", sum)

# Funktion ausführen mit n von Nutzer
sum(n)
