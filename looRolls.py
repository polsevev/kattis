k = input()
d = k.split(" ")
lengdeRull = int(d[0])
lengdePrTur = int(d[1])
rest = 0
i = 0
while True:
    if rest == 0 and i != 0:
        break
    else:

        lengdePrTur = lengdePrTur-rest

    i = i+1

print(i)
