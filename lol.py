a = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
g = []
d = []
for b in range(0, len(a)):
    g.append([])
    for c in range(0, len(a[b])):
        g[b].append(0)
for b in range(0, len(a)):
    d.append([])
    for c in range(0, len(a[b])):
        d[b].append(1)
i = 0
while i < 5:
    i = i+1
    if g == d:
        break
    else:
        for n in range(0, len(a)):
            for f in range(0, len(a[n])):
                if a[n][f] == 1:
                    if n!=0:
                        g[n-1][f] = 1
                    if n != 2:
                        g[n+1][f] = 1
                    if f != 0:
                        g[n][f-1] = 1
                    if f != 3:
                        g[n][f+1] = 1
                print(a)
        a = []
        for b in range(0, len(g)):
            a.append([])
            for c in range(0, len(g[b])):
                a[b].append(g[b][c])
print(i)
print(g)
