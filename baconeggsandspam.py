for yikes in range(0, 100):
    a = int(input())
    if a == 0:
        break
    dicti = {}
    listOfKeys = []
    for n in range(a):
        b = input()
        c = b.split(" ")
        for d in range(1, len(c)):
            if c[d] in dicti:
                dicti[c[d]].append(c[0])

            else:
                dicti[c[d]] = [c[0]]
                listOfKeys.append(c[d])
    listOfKeys.sort()
    for n in listOfKeys:
        dicti[n].sort()
        b = " ".join(dicti[n])

        print(n, b)
    print("")
