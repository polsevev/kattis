apaxianNavn = input()

apaxianList = list(apaxianNavn)
antall = len(apaxianList)

i = 0
while i < antall-1:
    if apaxianList[i] == apaxianList[i+1]:
        apaxianList[i] = ""
    else:
        i = i+1

apaxianNavn = "".join(apaxianList)
print(apaxianNavn)