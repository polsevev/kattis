import operator
tall = input()
yoink = tall.split(" ")
antallPokemon = int(yoink[0])
antallPrKat = int(yoink[1])
attack = {}
defense = {}
hp = {}
for n in range(0, antallPokemon):
    boink = input()
    y = boink.split(" ")
    attack[n] = int(y[0])
    defense[n] = int(y[1])
    hp[n] = int(y[2])

pokemonsSomVant = []

for l in range(0, antallPrKat):
    d = (max(attack.items(), key=operator.itemgetter(1))[0])
    pokemonsSomVant.append(d)
    del attack[d]
    g = (max(defense.items(), key=operator.itemgetter(1))[0])
    pokemonsSomVant.append(g)
    del defense[g]
    f = (max(hp.items(), key=operator.itemgetter(1))[0])
    pokemonsSomVant.append(f)
    del hp[f]

g = list(set(pokemonsSomVant))
print(len(g))