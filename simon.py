numberOfTest = int(input())
if numberOfTest < 20:
    i = 0
    while i < numberOfTest:
        innTast = input()
        data = innTast.split(" ")
        if data[0] == "simon" and data[1] == "says":
            f = 2
            yoink = []
            while f < len(data):
                yoink.append(data[f])
                f = f+1
            s = " "
            print(s.join(yoink))

        else:
            print(" ")
        i = i+1
else:
    exit()
