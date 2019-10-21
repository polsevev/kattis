a = input()
b = list(a)
c = []
for n in range(0, len(b)):
    if b[n] == "<":
        c.pop(-1)
    else:
        c.append(b[n])
d = "".join(c)

print(d)