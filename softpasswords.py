S = input()
P = input()
accepted = False

if P == S:
   accepted = True
for n in range(0, 10):
    a = str(n) + P
    if a == S:
        accepted = True
        break
for n in range(0, 10):
    a = P + str(n)
    if a == S:
        accepted = True
        break
if P.swapcase() == S:
    accepted = True

if accepted:
    print("Yes")
else:
    print("No")
