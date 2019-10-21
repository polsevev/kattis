

numberOfCases = int(input())
for n in range(numberOfCases):
    userIn = int(input())
    number = 1
    for n in range(1, userIn+1):
        number = number*n
    b = list(str(number))
    print(b[-1])