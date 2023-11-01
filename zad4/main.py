###################
# Oliwia Rogowska #
#    Zadanie 4    #
#     Python      #
#   31.10.2023    #
###################

# zad 4.2

def ruler(length: int):
    if length <= 0 or not isinstance(length, int):
        raise ValueError("Please provide positive integer number greater than 0.")
    ruler1 = str(print("|...." * length, end="|"))
    ruler1.join(str(print()))
    for x in range(length + 1):
        ruler1.join(str(print(x, end=' ' * (5 - len(str(x + 1))))))
    ruler1.join(str(print("\n")))
    return ruler1


def net(height: int, width: int):
    if height <= 0 or width <= 0 or not isinstance(height, int) or not isinstance(width, int):
        raise ValueError("Please provide positive integer numbers greater than 0")
    net1 = ""
    for h in range(height):
        net1.join(str(print("+---" * width, end="*")))
        net1.join(str(print()))
        net1.join(str(print("|   " * width, end="|")))
        net1.join(str(print()))
    net1.join(str(print("*---" * width, end="*")))
    net1.join(str(print()))
    return net1


# zad 4.3
def factorial(n: int):
    if n < 0:
        raise ValueError("You need to provide positive number.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


# zad 4.4
def fibonacci(n: int):
    if n < 0:
        raise ValueError("You need to provide positive number.")
    a = 0
    b = 1
    for i in range(n):
        b += a
        a = b - a
    return a


# zad 4.5
def odwracanie(L: list, left: int, right: int):
    if left > right or left <= 0 or right <= 0 or left > len(L) or right > len(L):
        raise ValueError("Please provide positive values bigger than 0, left >= right.")
    right_range = int(right / 2 + 1)
    index = 1
    for i in range(left - 1, right_range):
        L[i], L[right - index] = L[right - index], L[i]
        index += 1
    return L


# zad 4.6
def sum_seq(sequence):
    if len(sequence) == 0:
        return 0
    elif isinstance(sequence[0], (list, tuple)):
        return sum_seq(sequence[0]) + sum_seq(sequence[1:])
    else:
        return sequence[0] + sum_seq(sequence[1:])


# zad 4.7
def flatten(sequence):
    if not (bool(sequence)):
        return sequence
    elif isinstance(sequence[0], (list, tuple)):
        return list(flatten(sequence[0])) + list(flatten(sequence[1:]))
    else:
        return sequence[:1] + flatten(sequence[1:])
