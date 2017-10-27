class Word:

    secret_word = ""
    which_letters_guessed = []
    strikes = 0

    def __init__(self, chosen_word="apple"):
        self.secret_word = chosen_word
        for _ in self.secret_word:
            self.which_letters_guessed.append(False)
        self.strikes = 0

    def contains(self, guessed_letter):
        if guessed_letter in self.secret_word:
            return True
        else:
            return False

    def evaluate(self, guess):
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
                for letter in self.which_letters_guessed:
                    self.which_letters_guessed[i] = True
                    i += 1

    def print(self):
        i = 0
        for letter in self.secret_word:
            if self.which_letters_guessed[i] is True:
                print(letter, end='')
            else:
                print('_', end='')
            i += 1

    def is_complete(self):
        for letter in self.which_letters_guessed:
            if letter is False:
                return False
        return True

    def drawMan(self):
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
                        print("   /  \\     |")
                        print("  /    \\    |")






