i = 0
while i < 1:
    tall = input()
    if tall != "0 0 0":
        yoink = tall.split()
        alleTall = []
        alleTall.append(int(yoink[0]))
        alleTall.append(int(yoink[1]))
        alleTall.append(int(yoink[2]))
        alleTall.sort()
        kat1 = alleTall[0]
        kat2 = alleTall[1]
        hyp = alleTall[2]

        if (kat1**2) + (kat2**2) == hyp**2:
            print("right")
        else:
            print("wrong")
    else:
        exit()