## Wizytówka
Jarosław Glegoła 
293092

## Problem
![zadanie](task_image.jpg)

## Parametry programu
### Mode 1 - dane z pliku - flaga = "-m1"
1. 
    -f -> nazwa pliku z którego chcemy wczytać dane
### Mode 2 - losowy przypadek flaga = "-m2"
1. -w - szerokość prostokąta
2. -ht - wysokość prostokąta
3. -p - liczba losowych punktów do wygenerowania
 
### Mode 3 - losowy przypadek flaga = "-m3"
1. -w - startowa szerokość prostokąta
2. -ht - startowa wysokość prostokąta
3. -p - startowa liczba losowych punktów do wygenerowania
4. -wstep - liczba o jaką będzie się zwiększać szerokość z każdą następną iteracją
5. -hstep - liczba o jaką będzie się zwiększać wysokość z każdą następną iteracją 
6. -pstep - liczba o jaką będzie się zwiększać liczba punktów z każdą następną iteracją 
7. -k - liczba iteracji
8. -r - liczba powtórzen każdej z iteracji

### Wybór algorytmu:
1. -bt - problem będzie rozwiązywany metododą brute force
2. -oi - problem będzie rozwiązywany metododą outside in
3. -io - problem będzie rozwiązywany metododą inside out

## Rozwiązanie problemu
Szczegółowe informacje w dokumentacji

Do rozwiązania problemu użyłem trzech sposobów:
1. Brute force - z pośród wszystkich dostępnych spełniających wymagania 1,2,4 wyszukaj największy z nich, który spełnia
wymaganie 3
2. Outside in - zaczynając od największego prostokąta, przesuwaj jego krawędzie do środka tym, samym zmniejszając jego powierzchnię
znajdz. Jeżeli aktualny prostokąt jest działką zapamiętaj i szukaj dalej. Zwróć największą działkę
3. Inside out - dla każdego punktu z P znajdz dla niego największą działkę która zawiera go w sobie

## Algorytmy i struktury danych
### Struktury danych
**FixedDeque** - autorska struktura danych implementująca wariację deque, czyli double-ended queue. Ma ona za zadanie dostarczać takiej
samej funkcjonalności jak zwykła deque, lecz kopiowanie jej ma być w stałym czasie + nie można dodawać do niej elementów.

### Algorytmy ze standardowej biblioteki
bisect - https://docs.python.org/2/library/bisect.html

insort - https://docs.python.org/2/library/bisect.html

## Przewodnik po plikach
```
.
├── data
│   ├── plots
│   │   ├── DrawSolution.py - klasa rysująca rozwiązanie na grafie
│   └── random_generator - pliki związane z generacją danych
│       └── random_problem.py
├── modes - pliki związane z wejściem użytkownika - flagi, parametry itp.
│   ├── command_line_config.py
│   ├── filemode
│   │   ├── FileMode.py
│   │   ├── FileReader.py
│   └── tablemode
│       ├── Analizer.py
└── solutions - pliki związane z rozwiązaniami problemu
    ├── BruteForceSolution.py - klasa rozwiącująca problem metodą brute force
    ├── PointsSolution.py - klasa rozwiącująca problem metodą Inside out
    ├── Solution.py - klasa rozwiącująca problem metodą Outside in
    └── models
        ├── FixedDeque.py - pomocnicza struktura danych używana w rozwiązaniu Outside in 
        ├── PointsQueue.py - pomocnicza klasa do rozwiązania problemu Outside in
        ├── Side.py - enum reprezentujący poszczególne boki prostokąta
        ├── Square.py - klasa reprezentująca prostokąt
```
