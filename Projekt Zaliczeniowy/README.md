## Projekt zaliczeniowy
### "Implementacja drzew czerwono-czarnych" - Python 23/24 - Oliwia Rogowska

Drzewa czerwono czarne to drzewa wyszukiwań binarnych, które spełniają
następujące warunki:

1. Każdy węzeł mam przypisany kolor: czerwony lub czarny.
2. Korzeń i liście (wartownicy) są czarne.
3. Czerwony węzeł nie może mieć czerwonego syna.
4. Na każdej ścieżce od korzenia do liści jest tyle samo
czarnych węzłów.

Projekt składa się z trzech plików:
1. [Node.py](https://github.com/rogowska/Python-2023-2024/blob/master/Projekt%20Zaliczeniowy/Node.py) zawiera klasę Node dla drzewa.
2. [RBTree.py](https://github.com/rogowska/Python-2023-2024/blob/master/Projekt%20Zaliczeniowy/RBTree.py) zawiera klasę drzewa czerwono-czarnego.
3. [test_RBTree.py](https://github.com/rogowska/Python-2023-2024/blob/master/Projekt%20Zaliczeniowy/test_RBTree.py) zawiera testy unitowe dla klasy RBTree.

Node przechowuje informacje o rodzicach, dzieciach, kolorze oraz wartości węzła. Porównanie węzłów odbywa się poprzez porównanie ich wartości, ponieważ nie akceptuje się duplikatów.

W klasie RBTree znajdują się metody:
1. __init__ - inicjuje korzeń nowego drzewa o podanej przez użytkownika wartości. Rodzicem korzenia jest wartownik.
2. __str__ - pozwala na wyświetlanie wartości węzłów w drzewie w kolejności inorder.
3. __search__ - funkcja znajdująca węzeł o danej wartości i zwracająca ten węzeł jeżeli istnieje, a w przeciwnym
        wypadku nil.
4. __minimum__ - funkcja znajdująca węzeł o najmniejszej wartości dla danego drzewa i zwracająca ten węzeł.
5. __maximum__ - funkcja znajdująca węzeł o największej wartości i zwracająca tą wartość.
6. __successor__ - funkcja zwracająca następnik węzła przy przeglądaniu węzła w kolejności inorder.
7. __predecessor__ - funkcja zwracająca poprzednik węzła przy przeglądaniu węzła w kolejności inorder.
8. __insert__ - funkcja pozwalająca wstawić węzeł o danej wartości do drzewa.
9. __delete__ - funkcja pozwalająca usunąć węzeł o danej wartości z drzewa.

Wstawianie (__insert__) odbywa się poprzez wstawienie węzła w odpowiednie miejsce i pokolorowanie go na czerwono, 
a następnie wykonanie funkcji sprawdzających, czy wszystkie warunki drzewa czerwono-czarnego są spełnione. Są cztery przypadki, kiedy 
warunki nie są spełnione. 
1. Wstawiany węzeł jest korzeniem - wówczas wystarczy przekolorować go na czarno.
2. Wój (brat rodzica węzła) jest czerwony - wówczas przekolorowywujemy ojca i wójka węzła na czarno, a dziadka na czerwono.
3. Wój jest czarny (w konfiguracji "trójkątnej" - węzeł jest prawym dzieckiem rodzica a rodzic lewym dzieckiem dziadka lub na odwrót) - wówczas rotujemy rodzica węzła w kierunku przeciwnym do węzła.
4. Wój jest czarny (w konfiguracji "w linii prostej" - węzeł jest lewym dzieckiem rodzica a rodzic lewym dzieckiem dziadka lub odwrotnie) - rotujemy dziadka węzła w kierunku przeciwnym do węzła i inwertujemy kolory
5. orginalnego rodzica i dziadka.

Usuwanie (__delete__) korzysta z funkcji pomocniczej __transplant__ która pozwala na przesuwanie poddrzew w drzewie. W usuwaniu rozważamy trzy przypadki:
1. Kiedy lewe dziecko nie istnieje - wywołujemy funkcję transplant na usuwanym węźle i na jego prawym dziecku.
2. Kiedy prawe dziecko nie istnieje wywołujemy funkcję transplant na usuwanym węźle i jego lewym dziecku.
3. Kiedy oba istnieją - wywołujemy funkcję transplant na węźle o najmniejszej wartości w prawym poddrzewie i jego liściu i potem drugi raz, tym razem wołając funkcję na wybranym do usunięcia węźle i "minimalnym" węźle.

Po wszystkich wywołaniach funkcji __transplant__ należy wywołać funcję pomocniczą, która pozwoli na skorygowanie drzewa (rekoloryzacja węzłów i rotacje) tak aby drzewo zachowywało swoje własności.

Delete, insert oraz funkcje pomocnicze do tych metod zostały zaimplementowane na podstawie książki "Wprowadzenie do algorytmów" T. H. Cormena.
