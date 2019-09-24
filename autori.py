
navn = [n for n in input().split("-")]
int = []
i = 0
while i < len(navn):
    int.append(navn[i][0])
    i += 1

print(*int, sep='')


