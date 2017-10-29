from Word import Word
import random

words = ["apple", "peach", "banana", "pumpkin", "strawberry", "melon", "orange"]

word = Word(words[random.randrange(0, 7)])
complete = False
print("Hello! Welcome to Hangman!\nPlease guess a letter or a word:")
word.print()
guess = input()
while not complete:
    word.evaluate(guess)
    word.drawMan()
    word.print()
    if word.is_complete():
        complete = True
    else:
        guess = input("\nGuess a letter or a word\n")
