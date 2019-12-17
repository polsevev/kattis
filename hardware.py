a = int(input())

for n in range(a):
    houseNumber = input()
    b = input()
    c = b.split(" ")
    numberOfAdresses = int(c[0])
    g = input()
    j = g.split(" ")
    listOfNumbers = []
    if j[0] == "+":
        for o in range(int(j[1]), int(j[2]), int(j[3])):
            listOfNumbers.append(str(o))
    print(listOfNumbers)