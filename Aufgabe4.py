
# Funktion, damit user 5 Messwerte (mw) eingeben kann
def eingabe():
    mw = []
    for i in range(5):
        wert = float(input(f"Geben Sie den {i+1}. Wert ein: "))
        mw.append(wert)
    return mw
    

# Berechnen
def mittelwert(mw):
    mittelwert = sum(mw) / len(mw)
    print("Der Mittelwert der Messwerte ist:", mittelwert)


mittelwert(mw=eingabe())