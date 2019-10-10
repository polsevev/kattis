a = input()
b = a.split(" ")
height = int(b[0])
width1 = int(b[1])
bricks = int(b[2])

c = input()
widthOfBricks = c.split(" ")
heightWeAreOn = 0
widthOfCurrentWall = 0
i = -1
for n in range(0, height):
    widthOfCurrentWall = 0
    while True:
        i = i+1
        widthOfCurrentWall = widthOfCurrentWall + int(widthOfBricks[i])
        if widthOfCurrentWall == width1:
            heightWeAreOn = heightWeAreOn +1
            break
        elif widthOfCurrentWall > width1:
            print("NO")
            exit()


if heightWeAreOn == height and widthOfCurrentWall == width1:
    print("YES")
else:
    print("NO")