brukerInn = input()
listeAvBrukerInn = brukerInn.split(" ")
x = int(listeAvBrukerInn[0])
y = int(listeAvBrukerInn[1])
weak = int(listeAvBrukerInn[2])
a = []
for n in range(0, y):
    a.append([])
    for d in range(0, x):
        a[n].append(0)
for n in range(0, weak):
    brukerInn = input()
    brukerListe = brukerInn.split(" ")
    x1 = int(brukerListe[1])
    y1 = int(brukerListe[0])
    a[x1-1][y1-1] = 1


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
i = 1
while True:

    if g == d:
        break
    else:
        for n in range(0, len(a)):
            for f in range(0, len(a[n])):
                if a[n][f] == 1:
                    if n!=0:
                        g[n-1][f] = 1
                    if n != y-1:
                        g[n+1][f] = 1
                    if f != 0:
                        g[n][f-1] = 1
                    if f != x-1:
                        g[n][f+1] = 1

        a = []
        for b in range(0, len(g)):
            a.append([])
            for c in range(0, len(g[b])):
                a[b].append(g[b][c])
        if i == 1 and g == d:
            break

        i = i + 1
print(i)
