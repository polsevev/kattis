a = int(input())
for n in range(0, a):
    b = input()
    c = b.split(" ")
    c = [float(x) for x in c]
    if c[0] * c[1] == c[2]:
        print("Possible")
    elif c[0] + c[1] == c[2]:
        print("Possible")
    elif c[0] - c[1] == c[2]:
        print("Possible")
    elif c[1] - c[0] == c[2]:
        print("Possible")
    elif c[0] / c[1] == c[2]:
        print("Possible")
    elif c[1] / c[0] == c[2]:
        print("Possible")
    else:
        print("Impossible")