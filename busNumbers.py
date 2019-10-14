numberOfBusses = 6
a = "180 141 174 143 142 175"
listOfBusses = a.split()
print(listOfBusses)
detSomSkalPrintes = []
for i in range(0, len(listOfBusses)):
    listOfBusses[i] = int(listOfBusses[i])
kjede = 1
listOfBusses.sort()
for n in range(1, numberOfBusses):
    if int(listOfBusses[n-1]) == int(listOfBusses[n])-1:
        kjede = kjede +1
    else:
        if kjede > 2:
            detSomSkalPrintes.append(listOfBusses[n-kjede])
            detSomSkalPrintes.append(listOfBusses[n-1])
        kjede = 1

for n in range(0, len(detSomSkalPrintes), 2):
    for c in range(int(detSomSkalPrintes[n]), int(detSomSkalPrintes[n+1]-1)):

        listOfBusses.remove(int(detSomSkalPrintes[c])+1)



