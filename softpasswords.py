a = input()
b = input()
isEqual = "No"

if b == a:
    isEqual = "Yes"

for n in range(0, 9):
    add = str(n) + b
    if add == a:
        isEqual = "Yes"
        break

for n in range(0, 9):
    add = b + str(n)
    if add == a:
        isEqual = "Yes"
        break

c = []
d = ""
for n in range(0, len(b)):
    if b[n].isupper():
        c.append(b[n].lower())
    elif b[n].islower():
        c.append(b[n].upper())
    elif 47 < ord(b[n]) < 58:
        c.append(b[n])
    d = "".join(c)

if d == a:
    isEqual = "Yes"
print(isEqual)

