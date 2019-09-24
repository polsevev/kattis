inpTime = [int(x) for x in input().split()]

maxMin = ((inpTime[0] * 60) + inpTime[1])
minMin = (maxMin - 45)
if minMin < 0:
    minMin = minMin + (24*60)
timer = int(minMin / 60)
minutter = int(minMin%60)
print(timer, minutter)

