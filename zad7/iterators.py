# Oliwia Rogowska #
#    Zadanie 7    #
#     Python      #
#   15.11.2023    #
###################
import itertools
import random

# zad 7.6

# (a)
it = itertools.cycle([1, 0])

# (b)

it2 = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

# (c)

days = [0, 1, 2, 3, 4, 5, 6]
it3 = itertools.cycle(days)
