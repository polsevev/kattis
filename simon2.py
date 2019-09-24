antallRunder = int(input())

i = 0
while i < antallRunder:
    resultat = []
    settning = str(input())
    settningListe = settning.split()
    if settningListe[0] == "Simon" and settningListe[1] == "says":
        b = 2
        while b < len(settningListe):
            resultat.append(settningListe[b])
            b = b+1
        k = " ".join(resultat)
        print(k)
        i = i+1
    else:
        i= i+1
