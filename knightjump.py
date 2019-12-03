a = input()
liste = []
for n in range(0, int(a)):
    b = input()

    liste.append(list(b))
print(liste)

for a in range(0, len(liste)):
    for b in range(0, len(liste[a])):
        