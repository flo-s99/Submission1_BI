
# Es gibt meines Wissens kein modul, welches numerische werte in worte umwandelt, daher lookup table
zahlen = ['null', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun']

def user_input():
    zahl = input("Bitte geben Sie eine vierstellige Zahl ein: ")
    return zahl

def int2string(zahl):
    # Man iteriert durch die Zahlen und nutzt die eingegeben Zahlen vom User um diese zahl als lookup int  zu nutzen, sprich 3 ist das 4. element in definierter liste an zahlen (weil start mit 0)
    string = [zahlen[int(ziffer)] for ziffer in zahl]
    print("-".join(string))

zahl = user_input()
int2string(zahl)