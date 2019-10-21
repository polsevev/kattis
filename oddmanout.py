a = int(input())
for n in range(0, a):
    b = int(input())
    c = input()
    d = c.split(" ")
    d = [int(x) for x in d]
    for g in range(0, len(d)):
        if d.count(d[g]) == 1:
            print("Case #" + str(n+1) + ": " + str(d[g]))
            break