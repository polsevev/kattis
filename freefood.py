antallGanger = int(input())
tallene = []
i = 0
while i < antallGanger:
    inter = input()
    k = inter.split()
    b = int(k[0])
    while b <= int(k[1]):
        tallene.append(b)
        b = b+1
    i = i+1

tallene = list(dict.fromkeys(tallene))
print(len(tallene))