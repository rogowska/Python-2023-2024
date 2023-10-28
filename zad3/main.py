###################
# Oliwia Rogowska #
#    Zadanie 3    #
#     Python      #
#   27.10.2023    #
###################
import itertools

#zad 3.1

#x = 2; y = 3
#if (x > y):
#   result = x
#else:
#   result = y #- semicolons shouldnt be there

#for i in "axby":
#   if ord(i) < 100:
#       print (i) - indents were missing

#for i in "axby": print (ord(i) if ord(i) < 100 else i) - correct

#zad 3.2

#L = [3, 5, 4] ; L = L.sort() - sort() returns None, it just modifies the original list
#x, y = 1, 2, 3 - too many values to assign
#X = 1, 2, 3 ; X[1] = 4 - X is not a list, its missing brackets
#X = [1, 2, 3] ; X[3] = 4 - list has 3 elements, to extend it you need to use built in functions like append or extend
#X = "abc" ; X.append("d") - string has no append function
#L = list(map(pow, range(8))) - pow() missing required argument 'exp' on position 2

#zad 3.3

for num in range(30):
        if(num%3 != 0):
            print(num)

print()

#zad 3.4

while(True):
    x = input("Enter a float number: ")
    try:
        if x == "stop":
            break
        x = float(x)
    except:
        print("An exception occurred, please enter a float number")
    else:
        print("Number x: ", x, "Third power of x: ", pow(x, 3))
        x = input("Enter a float number: ")

#zad 3.5

length = 20

print("|...."*length, end="|")
print()
for x in range(length + 1):
    print(x, end=' '*(5-len(str(x+1))))

print("\n")

#zad 3.6

height = 3
width = 5

for h in range(height):
    print("+---"*width, end="*")
    print()
    print("|   "*width, end="|")
    print()
print("*---"*width, end="*")

print()

#zad 3.8

a = [3, 4, 11, 0, 2, 4, 5, 3, 2]
b = [3, 0, 3, 4, 87, 1, 12]

print()
print(list(set(a).intersection(b)))

#zad 3.9

c = [x + y for x,y in itertools.zip_longest(a, b, fillvalue=0)]
print(c)

#zad 3.10

arabic = []
num = "CDXLIV"
roman1 = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic1 = [1, 5, 10, 50, 100, 500, 1000]

#ways to create a dictionary
#1 using dict comprehension
myDict = {roman1[i]: arabic1[i] for i in range(len(roman1))}
print("1st method creating dictionary: ", myDict)

#2 using dict constructor
myDict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
print("2nd method creating dictionary: ", myDict)

#3 explicitly

roman2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman3 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
print("3rd method creating dictionary: ", roman2)

#1st way to get the arabic number using dict
for x in num:
    arabic.append(roman2[x])

for y in range(len(arabic)-1):
    if (arabic[y] < arabic[y+1]):
       arabic[y+1] = arabic[y+1] - arabic[y]
       arabic[y] = 0

result = sum(x for x in arabic)
print("Arabic number: ", result)

#2nd way to get the number using dict
result = 0

while num:
    # try first two chars
    if num[:2] in roman3:
        result += roman3[num[:2]]
        # cut off first two chars
        num = num[2:]
    else:
        result += roman3[num[:1]]
        # cut off first char
        num = num[1:]

print("Arabic number (2nd method): ", result)





