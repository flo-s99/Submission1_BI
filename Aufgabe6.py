km = float(input("Gefahrene Kilometer: "))
ts = float(input("Verbrauchter Treibstoff (in l): "))


def verbrauch(km, ts):
    verbrauch_avg = ts / km * 100
    print("Der durchschnittliche Verbrauch ist:", verbrauch_avg, "Liter pro 100 Kilometer")

verbrauch(km, ts)

