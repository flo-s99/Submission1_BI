def is_isogram(word):
    # Ordentlich formatieren, errors wenn man dies nicht tut
    word = word.replace(" ", "").replace("-", "").replace(",", "").replace(".","")
    word = word.lower()
    # Überprüfe, ob alle Buchstaben gleich oft vorkommen
    return len(set(word)) == len(word)


wort = input("Bitte geben Sie ein Wort ein: ")

# Ausgabe
if is_isogram(wort):
    print("TRUE")
else:
    print("FALSE")

