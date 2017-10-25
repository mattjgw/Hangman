from Word import Word

word = Word("apple")
complete = False
print("Hello! Welcome to Hangman!\nPlease guess a letter:")
guess = input()
while not complete:
    if word.contains(guess):
        word.show_letter(guess)
    word.print()
    if word.is_complete():
        print("\nCongradulations! You have guessed the word correctly")
        complete = True
    else:
        guess = input("\nGuess another letter")