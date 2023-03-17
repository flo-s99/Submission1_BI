user_input = float(input("Gib eine Zahl ein"))

def check(user_input):
    if user_input % 2 == 0:
        print("Die Zahl", user_input, "ist gerade")
    else:
        print("Die Zahl", user_input, "ist ungerade")

check(user_input)
