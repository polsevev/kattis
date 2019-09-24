spiller0 = [n for n in input().split(" ")]
spiller1 = [n for n in input().split(" ")]
spiller2 = [n for n in input().split(" ")]
spiller3 = [n for n in input().split(" ")]
spiller4 = [n for n in input().split(" ")]

verdier = []

verdier.append((int(spiller0[0]) + int(spiller0[1]) + int(spiller0[2]) + int(spiller0[3])))
verdier.append((int(spiller1[0]) + int(spiller1[1]) + int(spiller1[2]) + int(spiller1[3])))
verdier.append((int(spiller2[0]) + int(spiller2[1]) + int(spiller2[2]) + int(spiller2[3])))
verdier.append((int(spiller3[0]) + int(spiller3[1]) + int(spiller3[2]) + int(spiller3[3])))
verdier.append((int(spiller4[0]) + int(spiller4[1]) + int(spiller4[2]) + int(spiller4[3])))

vinner = max(verdier)

i = 0
while i< len(verdier):
    if vinner == verdier[i]:
        vinnertallet = i+1
        print(vinnertallet, vinner)
        exit()
    else:
        i = i+1