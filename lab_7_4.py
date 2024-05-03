def make_generator(f):
    def generator():
        n = 1
        while True:
            yield f(n)
            n += 1
    return generator


# Funkcja Fibonacciego
def fibonacci(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print("Test 7_4 make_generator")
    print("Funkcja Fibonacciego")
    fibonacci_generator = make_generator(fibonacci)()  # Uzyskujemy generator
    for _ in range(10):
        print(next(fibonacci_generator), end=" ")
    print()

    print("Funkcja 2 ** (n - 1)")
    # Test funkcji make_generator z wyrażeniem lambda dla ciągu geometrycznego
    geometric_generator = make_generator(lambda n: 2 ** (n - 1))()   # Uzyskujemy generator
    for _ in range(10):
        print(next(geometric_generator), end=" ")
    print()
