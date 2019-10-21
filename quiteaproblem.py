try:
    while True:
        a = input().lower()
        if a == "":
            break
        b = a.split(" ")
        if "problem" in b:
            print("yes")
        else:
            print("no")
except EOFError:
    exit()

