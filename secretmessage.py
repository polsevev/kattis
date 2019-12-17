a = int(input())
for yikes in range(a):
    b = input()
    L = len(b)
    M = 0
    for n in range(L, L+100):
        if (int(n**0.5))**2 == n:
            M = n
            break
    for n in range(L, M):
        b += "*"

    liste = list(b)
    listeAvLister = []
    yikes = int(M**0.5)
    bikes = 0
    for n in range(0, int(M**0.5)):
        listeAvLister.append([])
        for b in range(bikes, yikes):
            listeAvLister[n].append(liste[b])
        yikes += int(M**0.5)
        bikes += int(M**0.5)
    sortedBitch = []
    

