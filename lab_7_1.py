from funkcje import *

if __name__ == '__main__':
    print("Test 7_1_a ilość liczb parzystych")
    print("liczba([6, 1, 12]): ", liczba([6, 1, 12]))  # Wynik: 2 (jest dwie liczby parzyste, liczba([6, 1, 12])
    print("liczba([3, 1, 6]): ", liczba([3, 1, 6]))  # Wynik: 1 (jest jedna liczba parzysta)
    print("liczba([3, 1, 9]): ", liczba([3, 1, 9]))  # Wynik: 0 (nie ma liczb parzystych)

    print()
    print("Test 7_1_b mediana")
    print("median([6, 1, 21, 2, 3, 4, 5, 2, 1]): ", median([6, 1, 21, 2, 3, 4, 5, 2, 1]))  # Wynik: 3
    print("median([6, 1, 21, 2, 3, 4, 5, 2]): ", median([6, 1, 21, 2, 3, 4, 5, 2]))  # Wynik: 3.5
    print("median([1, 100, 100, 100, 100]): ", median([1, 100, 100, 100, 100]))  # Wynik: 100

    print()
    print("Test 7_1_c pierwiastek")
    print("pierwiastek(3, epsilon=0.1): ", pierwiastek(3, epsilon=0.1))
    print("pierwiastek(3, 0.01): ", pierwiastek(3, 0.01))
    print("pierwiastek(3): ", pierwiastek(3))

    print()
