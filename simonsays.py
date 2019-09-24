antallRunder = int(input())

for n in range(0, antallRunder):
    settning = input()
    if settning.startswith("simon says"):
        y = settning.split(" ")
        boink = []
        for n in range(2, len(y)):
            boink.append(y[n])
        d = " ".join(boink)
        print(d)
    else:
        print()