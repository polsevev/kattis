yoink = int(input())
priceAllBooks = []
totPrice = 0
for n in range(0, yoink):
    priceAllBooks.append(int(input()))
priceAllBooks.sort()
y = int(len(priceAllBooks) % 3)


b = 0
while True:
    if y != b:
        totPrice = totPrice + priceAllBooks[0]
        del priceAllBooks[0]
        b = b+1
    else:
        break

b = int(len(priceAllBooks) / 3)

i = 0

if yoink > 2:
    while len(priceAllBooks) != 0:
        totPrice = totPrice + priceAllBooks[len(priceAllBooks)-1] + priceAllBooks[len(priceAllBooks)-2]

        del priceAllBooks[-2]
        del priceAllBooks[-1]
        del priceAllBooks[0]

        i = i+1
print(totPrice)
