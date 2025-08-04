📘 Day 01 – Corner Cases and Testing Notes

This file documents the edge cases and test scenarios for the functions implemented in `exercises.py`.

---

🔢 `is_prime(n)`
- ❗ Test with 0 and 1 (should return False)
- ❗ Test with negative numbers (should return False)
- ✅ Test small primes: 2, 3, 5, 7
- ❓ Test large prime numbers (e.g., 97, 101)

---

🔁 `fibonacci_upto(n)`
- ❗ Test with 0 (should return `[0]`)
- ✅ Test with positive `n` like 10 or 20
- ❓ Test with negative input (optional: return empty or raise exception)

---

🧪 `is_palindrome(s)`
- ✅ Case sensitivity: `"Radar"` vs `"radar"`
- ✅ Even vs odd length strings: `"abba"` vs `"aba"`
- ❓ Whitespace: `"nurses run"` – should strip or normalize?

---

➕ `calculator(a, b, operation)`
- ❗ Division by zero (should return error message)
- ❗ Unknown operation (should return "Invalid operation")
- ✅ Test all operations: add, sub, mul, div

---

🔣 `count_vowels(s)`
- ✅ Mixed case input: `"AuToMoTiVe"`
- ❗ Empty string
- ❓ String with no vowels

---

📦 `sort_dict_by_value(d)`
- ✅ Already sorted dict
- ❗ Empty dictionary `{}`  
- ❓ Dictionary with same values (e.g., all 0s)

---

🧮 `common_elements_with_counts(list1, list2)`
- ❗ One list is empty
- ✅ Duplicates present in both
- ❓ No overlap between lists

---

🔍 `unique_elements(list1, list2)`
- ✅ Lists with completely different elements
- ❗ One list is empty

---

🎯 `find_common_elements(list1, list2)`
- ❗ Order independence
- ✅ Shared subset and no overlap
- ❗ Type mismatch: numbers vs strings

---

✳️ `number_pyramid(n)`
- ❗ `n=0` or negative (should return nothing or a message)
- ✅ `n=1` or `n=5`
- ❓ Very large `n` (formatting test)

---
