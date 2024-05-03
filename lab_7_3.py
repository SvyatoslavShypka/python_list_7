import random
import string


class PasswordGenerator:
    def __init__(self, length, charset=None, count=float('inf')):
        self.length = length
        self.charset = charset if charset else string.ascii_letters + string.digits
        self.count = count
        self.generated_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_count >= self.count:
            raise StopIteration
        password = ''.join(random.choice(self.charset) for _ in range(self.length))
        self.generated_count += 1
        return password


if __name__ == '__main__':
    print("Test 7_3 generator")
    generator_hasla = PasswordGenerator(length=10, count=4)
    print("Test metody next() wywołanej jawnie:")
    print("hasło 1: ", next(generator_hasla))
    print("hasło 2: ", next(generator_hasla))
    print("hasło 3: ", next(generator_hasla))
    print("hasło 4: ", next(generator_hasla))

    print("\nTest pętli for:")
    for haslo in PasswordGenerator(length=10, count=3):
        print(haslo)

    print("hasło 5 podnosi wyjątek, gdy nie ma następnego elementa: ", next(generator_hasla))  # Wyjątek StopIteration zostanie podniesiony po wygenerowaniu hasła > count
