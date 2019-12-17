a = input()
b = a.split(" ")
T = int(b[1])
n = int((b[0]))

c = input()
d = c.split(" ")
g = []
for h in range(0, len(d)):
    g.append(int(d[h]))



antallBrukt = 0
runder = 0
for j in range(n):
    antallBrukt += g[j]
    if antallBrukt <= T:
        runder += 1

print(runder)
