import argparse
from exercises import (
    swap_variables,
    is_prime,
    fibonacci_series,
    count_vowels,
    find_max,
    is_palindrome,
    calculator,
    sort_dict_values,
    find_common_preserve_order,
    common_elements_with_counts,
    unique_elements,
)

def main():
    parser = argparse.ArgumentParser(description="Run Python Day 01 exercises")
    parser.add_argument("--task", type=str, required=True, help="Exercise name (e.g., prime, fibonacci, palindrome)")

    args = parser.parse_args()
    task = args.task.lower()

    if task == "swap":
        print("Swap (3, 5):", swap_variables(3, 5))
    elif task == "prime":
        print("Is 13 prime?:", is_prime(13))
    elif task == "fibonacci":
        print("Fibonacci up to 20:", fibonacci_series(20))
    elif task == "vowels":
        print("Vowels in 'Automotive':", count_vowels("Automotive"))
    elif task == "max":
        print("Max in [3, 7, 1]:", find_max([3, 7, 1]))
    elif task == "palindrome":
        print("Is 'radar' a palindrome?:", is_palindrome("radar"))
    elif task == "calc":
        print("10 / 2 =", calculator(10, 2, "div"))
    elif task == "sort_dict":
        sample = {"x": 2, "y": 1}
        print("Sorted dict:", sort_dict_values(sample))
    elif task == "common":
        a = [1, 2, 3, 4]
        b = [3, 4, 5]
        print("Common:", find_common_preserve_order(a, b))
    elif task == "common_counts":
        a = [1, 2, 2, 3]
        b = [2, 2, 3, 4]
        print("Common with counts:", common_elements_with_counts(a, b))
    elif task == "unique":
        a = [1, 2, 3]
        b = [3, 4, 5]
        print("Unique:", unique_elements(a, b))
    else:
        print("Unknown task. Try: swap, prime, fibonacci, vowels, max, palindrome, calc, sort_dict, common, common_counts, unique")

if __name__ == "__main__":
    main()
