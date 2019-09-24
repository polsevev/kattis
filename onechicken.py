HOREBUKK = input()
listeAvTall = HOREBUKK.split()
mennesker = int(listeAvTall[0])
kylling = int(listeAvTall[1])

diff = kylling - mennesker

if diff == 0:
    exit()

if diff > 0:
    if diff == 1:
        print("Dr. Chaz will have" + diff + " piece of chicken left over!")
    else:
        print("Dr. Chaz will have", diff, "pieces of chicken left over!")
elif diff < 0:
    if diff == -1:
        print("Dr. Chaz needs", - diff, "more piece of chicken!")
    else:
        print("Dr. Chaz needs", - diff, "more pieces of chicken!")