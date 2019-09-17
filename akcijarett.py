b = int(input())
priser = []
for n in range(0, b):
    priser.append(int(input()))
priser.sort(reverse = True)

y = (len(priser)%3)
tot = 0
for n in range(0, y):
    tot = tot + priser[-1]
    del priser[-1]

gruppe = []


for n in range(0, int(len(priser))):
    gruppe.append(priser[n])
    if len(gruppe) == 3:
        gruppe.sort()
        del gruppe[0]
        tot = tot + gruppe[1] + gruppe[0]
        del gruppe[0]
        del gruppe[0]
print(tot)
