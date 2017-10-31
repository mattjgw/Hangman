class Word:

    secret_word = ""
    which_letters_guessed = []
    strikes = 0

    def __init__(self, chosen_word="apple"):
        self.secret_word = chosen_word
        self.which_letters_guessed = []  # Ensures the which letters guessed list is empty before appending
        for _ in self.secret_word:
            self.which_letters_guessed.append(False)
        self.strikes = 0

    def evaluate(self, guess):  # Checks to see the result of the guess
        if len(guess) is 1:
            if self.secret_word.__contains__(guess):
                i = 0
                for letter in self.secret_word:
                    if letter == guess:
                        self.which_letters_guessed[i] = True
                    i += 1
            else:
                self.strikes += 1

        else:
            if guess == self.secret_word:
                i = 0
                for _ in self.which_letters_guessed:
                    self.which_letters_guessed[i] = True
                    i += 1
            else:
                self.strikes += 1

    def print(self):  # Prints the word with proper letters and blanks
        i = 0
        for letter in self.secret_word:
            if self.which_letters_guessed[i] is True:
                print(letter, end='')  # Print the letters so as to not print with a new line
            else:
                print('_', end='')  # Print the blanks so as to not print with a new line
            i += 1

    def is_complete(self):  # Checks to see if the game is complete
        if self.strikes >= 4:
            print("\nOh no! You've hung the man. Better luck next time")
            return True
        for letter in self.which_letters_guessed:
            if letter is False:
                return False
        else:
            print("\nCongratulations! You have deduced the word")
            return True

    def draw_man(self):  # Draws the hangman based on the strike count
        if self.strikes is 0:
            return
        elif self.strikes >= 1:
            print("_____________")
            print("    |       |")
            print("( ͡° ͜ʖ ͡°)    |")
            print("    ^       |")
            if self.strikes >= 2:
                print("    |       |")
                print("    |       |")
                if self.strikes >= 3:
                    print(" ___|___    |")
                    print("    |       |")
                    if self.strikes >= 4:
                        print("   / \\      |")
                        print("  /   \\     |")






