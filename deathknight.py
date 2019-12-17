a = int(input())
numberOfWin = 0
for n in range(0, a):
    b = input()
    win = True
    if "CD" in b:
        win = False
    if win:
        numberOfWin +=1
print(numberOfWin)
