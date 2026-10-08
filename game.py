import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def show_history(self):
        print("\nGuess History:")
        for number, (guess, feedback) in enumerate(self.history, start=1):
            print(f"{number}. {guess} -> {' '.join(feedback)}")

    def show_summary(self, result):
        print("\n--- Session Summary ---")
        print(f"Word length: {self.length}")
        print(f"Guesses used: {len(self.history)}")
        print(f"Result: {result}")

        if result == "Won":
            print(f"Solved in {len(self.history)} guess(es)!")
        elif result == "Lost":
            print(f"The word was: {self.target}")
        else:
            print("Game ended by the player.")

        print("-----------------------")

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")

        accepted_guesses = 0

        while accepted_guesses < 6:
            guess = input("> ").strip().lower()

            # Allow the player to quit without using a turn.
            if guess == "q":
                self.show_history()
                self.show_summary("Quit")
                return

            # Invalid guesses do not consume a turn
            # and are not added to history.
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            # This is an accepted guess.
            accepted_guesses += 1

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(" ".join(feedback))

            # Display history after every accepted guess.
            self.show_history()

            # Win condition.
            if guess == self.target:
                print("Solved!")
                self.show_summary("Won")
                return

        # Six accepted guesses were used without solving.
        print("Out of guesses!")
        print("The word was:", self.target)
        self.show_history()
        self.show_summary("Lost")


if __name__ == "__main__":
    WordleGame().run()