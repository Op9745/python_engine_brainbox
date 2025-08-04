# Python basics and logic building
from collections import Counter
# 1 : Swap two variables

def swap_variables(a, b):
    return b, a


# 2 : Check if a no is prime

def is_prime(n):
    # To start checking from 2
    if n <= 1:
        return False
    # Check for the no whether prime or not (Factorial Method)    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not a prime" #False condition
    return "Prime no"  # True condition also could be used


# 3 : Fiboncci Series upto n

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series


# 4 : Count vowels in a string

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")


# 5 : Find max value in a list

def find_max(lst):
    return max(lst) if lst else None


# 6 : CHeck if string is palindrome

def is_palindrome(s):
    return s == s[::-1]


# 7 : Create a simple calculator

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b if b != 0 else "Error: Division by zero"
    else: 
        return "Invalid Operation"
    
# 8 : Reverse a list without(slicing/.reverse())

def reversed_lst(lst):
    length = len(lst)
    s = length

    new_list = [None] * length

    for item in lst:
        s = s - 1
        new_list    [s] = item
    return new_list
    

# 9 : Number Pyramid

def number_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(' ' * (n - i), end='')
        # Print the number sequence for this row
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Move to next line


# 10 : Sort dict by values

def sort_dict_values(d, descending = False):
    return dict(sorted(d.items(), key= lambda item: item[1], reverse=descending))


# 11 : Common elements between two lists

def find_common_preserve_order(list1, list2):
    return [item for item in list1 if item in list2]


# 12 : Find common elements with counts using collections.Counter

def common_elements_with_counts(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    common = c1 & c2  # Intersection with counts
    return list(common.elements())


# 13 : Find unique elements between two lists (symmetric difference)

def unique_elements(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))
    

# 14 : write a custom split() function (like str.split())

def custom_split(s, delimiter=None):
    result = []
    word = ''
    
    if delimiter is None:
        # Default behavior: split on any whitespace
        i = 0
        while i < len(s):
            # Skip leading whitespace
            while i < len(s) and s[i].isspace():
                i += 1
            # Start of a word
            start = i
            while i < len(s) and not s[i].isspace():
                i += 1
            if start < i:
                result.append(s[start:i])
    else:
        i = 0
        while i < len(s):
            if s[i:i+len(delimiter)] == delimiter:
                result.append(word)
                word = ''
                i += len(delimiter)
            else:
                word += s[i]
                i += 1
        result.append(word)  # Add the last segment
    
    return result





if __name__ == "__main__":
    print(swap_variables(3, 5))
    print(is_prime(13))
    print(fibonacci_series(20))
    print(count_vowels("Automotive"))
    print(find_max([9, 3, 11, 2]))
    print(is_palindrome("radar"))
    print(calculator(10, 0, "div"))
    print(reversed_lst([1, 4, 5, 50, 7]))
    number_pyramid(7)
    # Sort dict by values
    scores = {
        "Alice": 82,
        "Bob": 95,
        "Charlie": 78,
        "David": 90
    }
    print("Ascending:", sort_dict_values(scores))
    print("Descending:", sort_dict_values(scores, descending=True))
    #Common elements between two lists preserve order
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]

    print("Common elements:", find_common_preserve_order(a, b))
    a = [1, 2, 2, 3, 4]
    b = [2, 2, 3, 5, 6]
    print("Common with counts:", common_elements_with_counts(a, b)) # Find common elements with counts using collections.Counter
    print("Unique elements:", unique_elements(a, b)) #Find unique elements between two lists (symmetric difference)
    #write a custom split() function (like str.split())
    print(custom_split("one,two,three", ","))       # ['one', 'two', 'three']
    print(custom_split("a b   c"))                  # ['a', 'b', 'c']
    print(custom_split("abc--def--ghi", "--"))      # ['abc', 'def', 'ghi']
    print(custom_split("  hello   world  "))        # ['hello', 'world']
    print(custom_split(""))                         # []
    print(custom_split(",,", ","))                  # ['', '', '']
