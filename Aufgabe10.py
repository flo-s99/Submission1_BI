schraube = 0.09
mutter = 0.03
beilagscheibe = 0.02

countS = int(input("Anzahl der Schrauben: "))
countM = int(input("Anzahl der Muttern : "))
countB = int(input("Anzahl der Beilagscheiben: "))

price_final = schraube * countS + mutter * countM + beilagscheibe * countB

# Runden auf 2 Nachkommastellen damit Output Format = Input Format
print(f"Gesamtpreis: {price_final:.2f} Euro")
