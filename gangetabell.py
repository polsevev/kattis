i = 1

while i <= 1000:
    b = 1
    boink = []
    while b <= 1000:
        boink.append("%9d" % (b*i))
        b = b+1
    d = " ".join(boink)
    print(d)
    i = i+1