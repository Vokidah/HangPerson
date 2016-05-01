class HangPersonGame:

    def __init__(self, word, guesses=None, wrong_guesses=None):
        self.word = word
        self.guesses = guesses
        self.wrong_guesses = wrong_guesses

    def guess(self, letter):
        if not letter or not letter.isalpha():
            return False
        letter.lower()
        if letter in self.word:
            if self.guesses and letter in self.guesses:
                return False
            elif not self.guesses:
                self.guesses = letter
            else:
                self.guesses += letter
        else:
            if self.wrong_guesses and letter in self.wrong_guesses:
                return False
            elif not self.wrong_guesses:
                self.wrong_guesses = letter
            else:
                self.wrong_guesses += letter
        return True

    def word_with_guesses(self):
        result = ""
        for each in self.word:
            if self.guesses and each in self.guesses:
                result += each
            else:
                result += '-'
        return result

    def check_win_or_lose(self):
        if self.wrong_guesses and len(self.wrong_guesses) >= 7:
            return 0
        elif self.word == self.word_with_guesses():
            return 1
        else:
            return 2

