## 1. Print every character in the string 'Camus'

word = "Camus"

# first way
for w in word:
    print(w)

# second way
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])

# third way
print(
    word[0],
    word[1],
    word[2],
    word[3],
    word[4],
    )

## 2. Write a program that collects two strings from a user, inserts them into 
## the string "Yesterday I wrote a [response_one]. I sent it to [response_two]!"
## and prints a new string.

word1 = input("What you wrote yesterday: ")
word2 = input("Who did you send it to: ")

sentence = "Yesterday I wrote a {}. I sent it to {}.".format(word1, word2)
print(sentence)


## 3. Use a method to make the string 'aldous Huxley was born in 1894.' 
## grammatically correct by capializing the first letter in the sentence.

correct = "aldous Huxley was born in 1894.".capitalize()

print(correct)


## 4. Take the string 'Where now? Who now? When now?' and call a method that
## returns a list that looks like: ['Where now?', 'Who now?', 'When now?']

split_sentence = "Where now? Who now? When now?"

print(split_sentence.split("?"))

## 5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and
## turn it into a grammatically correct string. There should be a space between
## the word fence and the period that follows it.

words = ["The", "fox", "jumped", "over", "the", "fence", "."]

fox = " ".join(words)
fox = fox[0:-2] + '.'
print(fox)


## 6. Replace every instance of 's' in 'A screaming comes across the sky.' with
## a dollar sign '$'

sentence = "A screaming comes across the sky."
sentence = sentence.replace("s", "$")
print(sentence)


## 7. Use a method to find the first index of the character 'm' in the string
## 'Hemingway'

word = "Hemingway".index('m')

print(word)


## 8. Find dialogue in your favorite book (containing quotes) and turn it into 
## a string

sherlock_holmes = """'Well, Watson, what do you make of it?' - Holmes was
sitting with his back to me, and I had given him no sign of my occupation.
'How did you know what I was doing? I believe you have eyes in the back
of your head?'
"""
print(sherlock_holmes)


## 9. Create the sting 'three three three' using concatenation, and then again
## using multiplication

three_concat = 'three ' + 'three ' + 'three'
three_mult = 'three ' * 3
print(three_concat)
print(three_mult)

## 10. Slice the string 'It was a bright cold day in April, and the clocks were 
## striking thirteen.' to only include the characters before the comma

sentence = "It was a bright cold day in April, and the clocks were striking\
 thirteen."

sentence = sentence[0:33]

print(sentence)