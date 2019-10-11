a = input()
b = a.split(" ")
rows = int(b[0])
column = int(b[1])
start = int(b[2])
map = []
for n in range(0, column):
    map.append([])
    for a in range(0, rows):
        map[n].append(0)
listOfWeak = []
for c in range(0, start):
    a = input()
    b = a.split(" ")
    listOfWeak.append([int(b[0])-1, int(b[1])-1])

for a in range(0, len(listOfWeak)):
    map[listOfWeak[a][1]][listOfWeak[a][0]] = 1
teller = 0
while True:
    summen = 0
    if len(map)*len(map[0]) == summen:
        break
    for a in range(0, len(map)):
        for b in range(0, len(map[a])):
            if map[a][b] == 1:
                if a-1 >=0:
                    map[a-1][b] = 1
                if a+1 <= column-1:
                    map[a + 1][b] = 1
                if b-1 >= 0:
                    map[a][b-1] = 1
                if b+1 <= rows -1:
                    map[a][b+1] = 1

    for n in range(0, len(map)):
        print(map[n])
        summen = summen + sum(map[n])
    print(summen)
    if summen == 12:
        break
    teller = teller +1

print(teller)



