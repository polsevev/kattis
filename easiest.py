N = []
boink = []
i = 0
while i < 1:
    a = input()
    b = int(a)
    if b == 0:
        i = i+1
    else:
        N.append(a)

i = 0
while i < len(N):
    a = 0
    b = 0
    while b < len(N[i]):
        a = a + int(N[i][b])
        b = b+1
    boink.append(a)

    i = i+1
i = 0
while i < len(boink):
    if boink[i] < 10:
        boink[i] = 10
    i = i+1

i = 0
while i < len(N):
    b = 10
    while b < int(N[i]):
        M = str((int(N[i])) * b)
        c = 0
        a = 0
        w = []
        while c < len(M):
            a = a + int(M[c])
        w.append(a)
        if w == boink[i]:
            print(b)
        else:
            b=b+1
    i=i+1