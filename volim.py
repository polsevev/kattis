Spiller = int(input())

antallSporsmål= int(input())

totTime = 210

i = 0

while i < antallSporsmål:
    yoink = input()
    boink = yoink.split()
    tidBrukt = int(boink[0])
    totTime = totTime - tidBrukt
    if totTime > 0:

        omVidere = boink[1]

        if omVidere == "T":
            if Spiller == 8:
                Spiller = 1
            else:
                Spiller = Spiller+1
    else:
        break

print(Spiller)
