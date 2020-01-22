board = []

valid = True
for i in range(0, 8):
    a = input()
    b = list(a)
    board.append(b)

for a in range(0, len(board)):
    for b in range(0, len(board[a])):
        if board[a][b] == "*":
            rowCounter = 0
            for i in range(0, len(board) - (a+1)):
                c = i + (b-a)
                if board[rowCounter][c] == "*":
                    valid = False
                rowCounter += 1
            rowCounter = b+a
            g = 0
            while True:
                print(rowCounter, g)
                if rowCounter < 0:
                    break
                if board[rowCounter][g] == "*":
                    valid = False
                rowCounter -= 1
                g += 1
            for i in range(0, len(board)):
                



print(valid)


