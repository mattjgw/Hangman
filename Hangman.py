from Word import Word
import random

words = ["apple", "peach", "banana", "pumpkin", "strawberry", "melon", "orange"]
play = True

while play:
    word = Word(words[random.randrange(0, 7)])  # Create a word object using a random word from the words list
    complete = False
    print("Hello! Welcome to Hangman!\nPlease guess a letter or a word:")
    word.print()
    guess = input()
    while not complete:
        word.evaluate(guess)
        word.draw_man()
        word.print()
        if word.is_complete():
            complete = True
            answer = input("Would you like to play again? (Answer yes or no)")
            if answer.lower() == "yes":
                continue
            else:  # If user answers anything but yes, do not play again
                play = False

        else:
            guess = input("\nGuess a letter or a word\n")
print("Goodbye!")
