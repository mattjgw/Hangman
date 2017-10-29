from Word import Word

word = Word("apple")
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
