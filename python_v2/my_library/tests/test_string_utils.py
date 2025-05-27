# python_v2/my_library/tests/test_string_utils.py
import unittest
from python_v2.my_library.string_utils import reverse_string, capitalize_string, is_palindrome, count_vowels, remove_spaces, reverse_words

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("world"), "World")
        self.assertEqual(capitalize_string(""), "")
        self.assertEqual(capitalize_string("HELLO"), "Hello")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("Rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("hello world"), "helloworld")
        self.assertEqual(remove_spaces(" no spaces here "), "nospaceshere")
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("singleword"), "singleword")

    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("one two three"), "three two one")
        self.assertEqual(reverse_words("single"), "single")
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("  leading and trailing spaces  "), "  spaces trailing and leading  ") # Preserves multiple spaces between words

    def test_reverse_words_with_multiple_spaces(self):
        """Tests reverse_words with multiple spaces between words and leading/trailing spaces."""
        self.assertEqual(reverse_words("  hello   world  "), "  world   hello  ")
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("   "), "   ") # Only spaces
        # New test case (from previous turn, ensure it's still here if you removed it)
        self.assertEqual(reverse_words(" single word "), " word single ") # This is the one that was causing the error