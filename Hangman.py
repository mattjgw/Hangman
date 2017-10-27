from Word import Word

word = Word("apple")
complete = False
print("Hello! Welcome to Hangman!\nPlease guess a letter or a word:")
guess = input()
while not complete:
    word.evaluate(guess)
    word.drawMan()
    word.print()
    if word.is_complete():
        print("\nCongratulations! You have guessed the word correctly")
        complete = True
    else:
        guess = input("\nGuess a letter or a word\n")

word = Word("apple")

word.drawMan()
