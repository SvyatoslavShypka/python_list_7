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
    # Obliczamy indeksy środkowych elementów
    middle_left_index = n // 2 - 1 if n % 2 == 0 else n // 2
    middle_right_index = n // 2 if n % 2 == 0 else None
    # Obliczamy medianę
    median_value = (lista_posortowana[middle_left_index] + lista_posortowana[middle_right_index]) / 2 if middle_right_index else lista_posortowana[middle_left_index]
    return median_value


def pierwiastek(x, epsilon=0.0001, y=None):
    # Początkowe przybliżenie pierwiastka
    y = x if y is None else y
    # Sprawdzenie warunku stopu
    if abs(y * y - x) <= epsilon:
        return y
    # Ulepszanie przybliżenia za pomocą rekurencji
    return pierwiastek(x, epsilon, 0.5 * (y + x / y))


def make_alpha_dict(text):
    wynik = {}
    # Dzielimy na słowa
    slowa = text.split()
    # Unikatowe znaki występujących w tekście
    znaki_unikatowe = set(c for slowo in slowa for c in slowo if c.isalpha())
    # Iteracja po unikatowych znakach i tworzenie list słów zawierających ten znak
    for znak in znaki_unikatowe:
        wynik[znak] = [slowo for slowo in slowa if znak in slowo]

    return wynik


def flatten(lista):
    wynik = []

    # Rekurencyjnie spłaszczamy listę
    def flatten_rekurencja(zagniezdziona_lista):
        for item in zagniezdziona_lista:
            if isinstance(item, (list, tuple)):
                flatten_rekurencja(item)  # Rekurencyjne wywołanie
            else:
                wynik.append(item)  # Dodanie elementu skalaru do wynikowej listy

    flatten_rekurencja(lista)
    return wynik


def forall(pred, iterable):
    return all(pred(x) for x in iterable)


def exists(pred, iterable):
    return any(pred(x) for x in iterable)


def atleast(n, pred, iterable):
    return sum(1 for x in iterable if pred(x)) >= n


def atmost(n, pred, iterable):
    return sum(1 for x in iterable if pred(x)) <= n
