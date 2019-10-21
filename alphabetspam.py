a = input()
b = list(a)
whitespaces = 0
lowercase = 0
uppercase = 0
symbols = 0
totalLength = float(len(b))
for n in range(0, len(b)):
    if ord(b[n]) == ord("_"):
        whitespaces = whitespaces +1
    elif ord("a")-1 < ord(b[n]) < ord("z")+1:
        lowercase = lowercase +1
    elif ord("A") -1 < ord(b[n]) < ord("Z")+1:
        uppercase = uppercase +1
    else:
        symbols = symbols +1
print(float(whitespaces) / totalLength)
print(float(lowercase) / totalLength)
print(float(uppercase) / totalLength)
print(float(symbols) / totalLength)
