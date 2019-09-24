total = [1, 1, 2, 2, 2, 8]
have = [int(x) for x in input().split()]

difference = []

for i in range(len(total)):
    difference.append((total[i] - have[i]))
    i=i+1
print(" ".join([str(x) for x in difference]))

