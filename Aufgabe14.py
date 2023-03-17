import random
import string

def generate_password(length, lower, upper, num, special_car):
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password_list = []
    for i in range(lower):
        password_list.append(random.choice(lowercase))
    for i in range(upper):
        password_list.append(random.choice(uppercase))
    for i in range(num):
        password_list.append(random.choice(digits))
    for i in range(special_car):
        password_list.append(random.choice(special))


    password_list += [random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length - len(password_list))]

    
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Wir haben folgendes Password generiert:", password)

# Benutzerinput
length = int(input("Wie lang soll das Passwort sein? "))
lower = int(input("Wie viele Kleinbuchstaben sollen enthalten sein? "))
upper = int(input("Wie viele Großbuchstaben sollen enthalten sein? "))
num = int(input("Wie viele Zahlen sollen enthalten sein? "))
special_car = int(input("Wie viele Sonderzeichen sollen enthalten sein? "))

generate_password(length, lower, upper, num, special_car)