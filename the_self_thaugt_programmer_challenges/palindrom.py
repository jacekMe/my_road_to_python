""" Check if the word is a palindrome.
A palindrome is a word that is the same when read from the front and back"""


def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(is_palindrome("Mum"))
print(is_palindrome("Kayak"))
