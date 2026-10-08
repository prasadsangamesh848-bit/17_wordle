import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")

        accepted_guesses = 0

        while accepted_guesses < 6:
            guess = input("> ").strip().lower()

            # Allow the player to quit without using a turn.
            if guess == "q":
                return

            # Invalid guesses do not consume a turn.
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            # This is an accepted guess, so now consume one turn.
            accepted_guesses += 1

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(" ".join(feedback))

            # Win condition.
            if guess == self.target:
                print("Solved!")
                return

        # Six accepted guesses were used without solving.
        print("Out of guesses!")
        print("The word was:", self.target)