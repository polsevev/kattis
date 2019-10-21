a = int(input())
tempsBelow0 = 0
b = input()
c = b.split(" ")
c = [ int(x) for x in c ]
for n in range(0, a):
    if c[n] < 0:
        tempsBelow0 = tempsBelow0 + 1
print(tempsBelow0)