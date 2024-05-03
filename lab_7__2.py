from funkcje import *


def is_odd(x):
    return x % 2 != 0


def is_negative(x):
    return x < 0


if __name__ == '__main__':
    print("Test 7_2 predykaty")
    # Przykładowe dane
    test_data_1 = [5, -7, 11, 23, -1]
    test_data_2 = [1, 2, -3, 4, 5]
    test_data_3 = [-10, 4, 8, -12, -6]

    print("Test funkcji forall:")
    print(f"forall(is_odd, {test_data_1}): ", forall(is_odd, test_data_1))  # True
    print(f"forall(is_odd, {test_data_2})", forall(is_odd, test_data_2))  # False
    print(f"forall(is_odd, {test_data_3})", forall(is_odd, test_data_3))  # False
    print()

    print("Test funkcji exists:")
    print(f"exists(is_odd, {test_data_1})", exists(is_odd, test_data_1))  # True
    print(f"exists(is_odd, {test_data_2})", exists(is_odd, test_data_2))  # True
    print(f"exists(is_odd, {test_data_3})", exists(is_odd, test_data_3))  # False
    print()

    print("Test funkcji atleast:")
    print(f"atleast(2, is_negative, {test_data_1})", atleast(2, is_negative, test_data_1))  # True
    print(f"atleast(2, is_negative, {test_data_2})", atleast(2, is_negative, test_data_2))  # False
    print(f"atleast(2, is_negative, {test_data_3})", atleast(2, is_negative, test_data_3))  # True
    print()

    print("Test funkcji atmost:")
    print(f"atmost(2, is_negative, {test_data_1})", atmost(2, is_negative, test_data_1))  # True
    print(f"atmost(2, is_negative, {test_data_2})", atmost(2, is_negative, test_data_2))  # True
    print(f"atmost(2, is_negative, {test_data_3})", atmost(2, is_negative, test_data_3))  # False
