def whoWins(antall):
    if antall % 2 == 0:
        return "Bob"
    else:
        return "Alice"

print(whoWins(int(input())))


