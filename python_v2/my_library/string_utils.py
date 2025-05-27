# python_v2/my_library/string_utils.py

def reverse_string(s: str) -> str:
    """Reverses a given string."""
    return s[::-1]

def capitalize_string(s: str) -> str:
    """Capitalizes the first letter of a string."""
    if not s:
        return ""
    return s.capitalize()

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome (reads the same forwards and backwards)."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s: str) -> int:
    """Counts the number of vowels (a, e, i, o, u, case-insensitive) in a string."""
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

def remove_spaces(s: str) -> str:
    """Removes all spaces from a string."""
    return s.replace(" ", "")

def reverse_words(s: str) -> str:
    """Reverses the order of words in a string."""
    words = s.split(" ")
    return " ".join(words[::-1])