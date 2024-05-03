def liczba(lista):
    # Używamy funkcji filter() w połączeniu z wyrażeniem lambda, aby zwrócić tylko parzyste liczby
    # Następnie przekształcamy wynik filter() w listę i zwracamy jej długość, która będzie równa liczbie liczb parzystych
    funkc_lambda = lambda x: x % 2 == 0
    wynik_filtrowany = filter(funkc_lambda, lista)
    wynik = list(wynik_filtrowany)
    ilosc_liczb_parzystych = len(wynik)
    return ilosc_liczb_parzystych


def median(lista):
    # Sortujemy listę
    lista_posortowana = sorted(lista)
    n = len(lista_posortowana)
    # Jeśli lista ma parzystą ilość - wynikiem będzie średnią arytmetyczną dwóch środkowych elementów
    if n % 2 == 0:
        middle_left = lista_posortowana[n // 2 - 1]
        middle_right = lista_posortowana[n // 2]
        return (middle_left + middle_right) / 2
    else:
        # Jeśli lista ma nieparzystą ilość - wynikiem będzie środkowy element
        return lista_posortowana[n // 2]


def pierwiastek(x, epsilon=0.0001, y=None):
    # Początkowe przybliżenie pierwiastka
    y = x if y is None else y
    # Sprawdzenie warunku stopu
    if abs(y * y - x) <= epsilon:
        return y
    # Ulepszanie przybliżenia za pomocą rekurencji
    return pierwiastek(x, epsilon, 0.5 * (y + x / y))
