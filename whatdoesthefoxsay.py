antall = int(input())

b = 0
while b < antall:
    i = 0
    avslutteLoop = ""
    listeAvLyder = []
    listeFjerning = []
    while avslutteLoop != "what does the fox say?":
        if i == 0:
            lyder = input()
            splitThisHoe = lyder.split(" ")
            d = 0
            while d < len(splitThisHoe):
                listeAvLyder.append(splitThisHoe[d])
                d = d+1
        else:
            avslutteLoop = input()
            splitThisBitch = avslutteLoop.split(" ")
            listeFjerning.append(splitThisBitch[2])
        i = i+1
    del listeFjerning[-1]
    c = 0
    while c < len(listeFjerning):
        f = 0

        while f < len(listeAvLyder):
            if listeAvLyder[f] == listeFjerning[c]:
                listeAvLyder[f] = ""
                print(listeAvLyder[f])
            f = f + 1
        c = c + 1
    while "" in listeAvLyder:
        listeAvLyder.remove("")
    t = " ".join(listeAvLyder)

    print(t)
    b = b+1
