f = input()
d = f.split(" ")
antallRuterY = int(d[0])
antallRuterX = int(d[1])
antallSvake = int(d[2])
dicti = {}
dictiSlutt = {}
loopDicti = {}
if antallRuterX == 0:
    print(0)
    exit()
elif antallRuterX < 0:
    antallRuterX = abs(antallRuterX)
for n in range(0, antallRuterY):
    dicti[n] = {}
    for q in range(0, antallRuterX):
        dicti[n][q] = 0

for n in range(0, antallRuterY):
    dictiSlutt[n] = {}
    for q in range(0, antallRuterX):
        dictiSlutt[n][q] = 1

for s in range(0, antallSvake):
    bruker = input()
    lol = bruker.split(" ")
    yoink = int(lol[0]) - 1
    boink = int(lol[1]) - 1
    dicti[yoink][boink] = 1

i = 1

while True:

    if dicti == dictiSlutt:
        break
    else:
        for n in range(0, len(dicti)):
            loopDicti[n] = {}
            for w in range(0, len(dicti[n])):
                loopDicti[n][w] = dicti[n][w]

        for a in range(0, antallRuterY):
            for b in range(0, antallRuterX):

                if loopDicti[a][b] == 1:
                    if a+1 < antallRuterY:

                        dicti[a+1][b] = 1
                    if a-1 > -1:

                        dicti[a-1][b] = 1
                    if b+1 < antallRuterX:

                        dicti[a][b+1] = 1
                    if b-1 > -1:

                        dicti[a][b-1] = 1
        i = i+1

print(i)
