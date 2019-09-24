antallGanger = int(input())
i = 0
while i < antallGanger:
    settning = str(input())
    settningUt = []
    settningListe = settning.split()
    if settningListe[0] == "simon" and settningListe[1] == "says":
        b = 2
        while b < len(settningListe):
            settningUt.append(settningListe[b])
            b = b+1
    s = " ".join(settningUt)
    print(s)
    i = i+1