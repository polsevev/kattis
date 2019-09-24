import numpy as np
yoink = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0,0,0,0,0]])
boink = np.array([[0,0], [0,0], [0,0], [0,0], [0,0]])
i = 0
while i <5:
    ekstra = [(i+1)]
    cheese = [0,0,0,0]
    cheese = [n for n in input().split(" ")]
    cheese.extend(ekstra)
    yoink[i] = cheese
    i = i+1
d = 0
while d < len(yoink):
    boink[d, 0] = (int(yoink[d, 0]) + int(yoink[d, 1]) + int(yoink[d, 2]) + int(yoink[d, 3]))
    boink[d, 1] = int(yoink[d, 4])
    d = d+1
vinnerVerdi = np.amax(boink)
g = 0
while g < len(boink):
    if vinnerVerdi == boink[g, 0]:
        print(boink[g, 1], boink[g, 0])
        exit()

