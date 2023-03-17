
def read_file():
    with open('file.txt', 'r') as f:
     txt = f.read()
     print(txt)
    count = txt.count("ein")
    count_Ein = txt.count("Ein")
    print("'ein' kommt", count, "mal vor.")
    print("Es gibt auch ein 'ein'", count, "mal am Satzanfang.")

read_file()
