numberOfCases = int(input())
tall = []
i = 0
while i < numberOfCases:
    tall.append(int(input()))
    i = i+1
b = 0
while b < len(tall):
    if tall[b] % 2 == 0:
        print(tall[b], "is even")
    else:
        print(tall[b], "is odd")
    b = b+1
