###################
# Oliwia Rogowska #
#    Zadanie 2    #
#     Python      #
#   20.10.2023    #
###################

line = ("Maria Wisława Anna Szymborska"
        " urodziła się na Prowencie,"
        " czyli folwarku położonym na południe od zamku w Kórniku,"
        " nad Jeziorem Kórnickim w Poznańskiem. GvR")

print(line)

#zad 2.10
wordsNumber = len(line.split())
print("Number of words:", wordsNumber)

#zad 2.11
w_o_r_d = '_'.join("word")
print(w_o_r_d)

#zad 2.12
listOfWords = line.split()

newWord = ''.join(word[0] for word in listOfWords)
print(newWord)

newWord2 = ''.join(word[len(word)-1] for word in listOfWords)
print(newWord2)

#zad 2.13
print("Sum of letters in string:", sum(len(word) for word in listOfWords))

#zad 2.14
longestWord = max(listOfWords, key=len)
print("Longest word in string:", longestWord)
print("Length of the word:", len(longestWord))

#zad 2.15
L = [4, 3, 5, 6, 3, 1, 4, 0, 8, 8, 5]
joined = ''.join(str(e) for e in L)
print(L, "Joined:", joined)

#zad 2.16
print("Adding Guido van Rossum:", line.replace("GvR", "Guido van Rossum"))

#zad 2.17
sortedWords = sorted(listOfWords)
print("Sorting with alphabetical order:", ' '.join(sortedWords))

sortedWords = sorted(listOfWords, key=len)
print("Sorting by length:", ' '.join(sortedWords))

#zad 2.18
number = 2334893478940918490410128490101001
print("Number of occurances of zeros in", number, ":", str(number).count('0'))

#zad 2.19
L = [42, 3, 533, 64, 301, 1, 4, 40, 822, 82, 5]
print(L, "String filled with zeros:", ' '.join(str(number).zfill(3) for number in L))