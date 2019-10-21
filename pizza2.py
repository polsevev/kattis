import math
a = input()
b = a.split(" ")
R = b[0]
C = b[1]

AR = float(R) ** 2 * 3.14
AC = (float(R) - float(C))**2 * 3.14

percent = (AC/AR) * 100

print("%6f" % percent)