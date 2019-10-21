while True:
    N = input()
    a = list(N)
    sum = 0
    for n in range(0, len(a)):
        sum = sum + int(a[n])
    N = int(N)
    if  N == 0:
        break
    else:
        i = 11

        while True:
            gange = N*i
            sum1 = 0
            g = list(str(gange))
            for n in range(0, len(g)):
                sum1 = sum1 + int(g[n])

            if sum1 == sum:
                print(i)
                break
            i = i +1