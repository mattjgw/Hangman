class Word:

    secret_word = ""
    which_letters_guessed = []

    def __init__(self, chosen_word="apple"):
        self.secret_word = chosen_word
        for _ in self.secret_word:
            self.which_letters_guessed.append(False)

    def contains(self, guessed_letter):
        if guessed_letter in self.secret_word:
            return True
        else:
            return False

    def show_letter(self, guessed_letter):
        i = 0
        for letter in self.secret_word:
            if letter == guessed_letter:
                self.which_letters_guessed[i] = True
            i += 1

    def print(self):
        print(self.which_letters_guessed)
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




