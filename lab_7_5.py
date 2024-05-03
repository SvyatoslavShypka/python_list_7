import functools
from lab_7_4 import fibonacci


def make_generator_mem(f):
    @functools.lru_cache(maxsize=None)  # Używamy lru_cache do memoizacji /None oznacza nielimitowana pamięć/
    def memoized_f(n):
        return f(n)

    def generator():
        n = 1
        while True:
            yield memoized_f(n)
            n += 1

    return generator


if __name__ == '__main__':
    print("Test 7_5 make_generator_mem")
    # Tworzymy generator z memoizacją dla funkcji fibonacci
    fibonacci_generator = make_generator_mem(fibonacci)()

    # Testujemy generator przez wyświetlenie kilku pierwszych wartości
    print("Pierwsze 10 wartości ciągu Fibonacciego:")
    for _ in range(10):
        print(next(fibonacci_generator), end=" ")
    print()
