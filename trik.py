brukerin = str(input())
rekke = list(brukerin)

ballpos = 1
i = 0
while i < len(rekke):
    if ballpos == 1:
        if rekke[i] == "A":
            ballpos = 2
        elif rekke[i] == "B":
            ballpos = 1
        else:
            ballpos = 3
    elif ballpos == 2:
        if rekke[i] == "A":
            ballpos = 1
        elif rekke[i] == "B":
            ballpos = 3
        else:
            ballpos = 2
    elif ballpos == 3:
        if rekke[i] == "A":
            ballpos = 3
        elif rekke[i] == "B":
            ballpos = 2
        else:
            ballpos = 1
    i = i+1
print(ballpos)