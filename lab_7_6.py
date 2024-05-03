import logging
from log import log

# Ustawienie konfiguracji loggera
logging.basicConfig(level=logging.DEBUG)


# Użycie dekoratora na funkcji
@log(level=logging.DEBUG)
def funkcja_dodawania(x, y):
    return x + y


# Użycie dekoratora na klasie
@log(level=logging.INFO)
class ExampleClass:
    def __init__(self, x, y):
        self.sum = x + y


if __name__ == '__main__':
    print("Test 7_6 dekorator")

    print("Test wywołania udekorowanej funkcji")
    print(funkcja_dodawania(4, 9))  # Wywołanie udekorowanej funkcji

    print("Test utworzenia instancji klasy")
    instancja_klasy = ExampleClass(3, 4)  # Utworzenie instancji klasy
    print(type(instancja_klasy))
