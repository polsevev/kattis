k = input()
d = k.split(" ")
numFrom = float(d[0])
fra = str(d[1])
til = str(d[3])


tilTh = {
    "th": 1,
    "thou": 1,
    "in": 1000,
    "inch": 1000,
    "ft": 12000,
    "foot": 12000,
    "feet": 12000,
    "yd": 36000,
    "yard": 36000,
    "ch": 792000,
    "chain": 792000,
    "fur": 7920000,
    "furlong": 7920000,
    "mi": 63360000,
    "mile": 63360000,
    "lea": 190080000,
    "league": 190080000
}


x = tilTh[fra] * numFrom

y = x / tilTh[til]

print(y)

