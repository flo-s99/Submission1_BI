def reverse(user_input):
    # Ertsmal ist input ein String und muss gesplittet werden in einzelne Wörter
    expression = user_input.split()
    # Values in der vAriable umdrehen
    expression.reverse()
    # Starten mit leerem String, dann wird die Liste an umgedrehten Wörtern in neuer variable zusammengeführt
    finalString = " ".join(expression)
    return finalString

user_input = input("Zeichenfolge (z.B. Hello World was yesterday): ")
print(reverse(user_input))
