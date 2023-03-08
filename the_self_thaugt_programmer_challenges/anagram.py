""" An anagram is a word formed by changing the order of the letters in the
original word. 
Check if the word is an anagram."""


def is_anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(is_anagram('below', 'elbow'))
print(is_anagram('young lady', 'an old guy'))
print(is_anagram('night', 'thing'))