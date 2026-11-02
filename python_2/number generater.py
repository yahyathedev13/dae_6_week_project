import random


def play_round() -> None:
	secret_number = random.randint(1, 100)
	attempts_left = 7

	print("\nI'm thinking of a number between 1 and 100.")
	print(f"You have {attempts_left} guesses. Type q to quit this round.")

	while attempts_left > 0:
		guess_text = input(f"\nYour guess ({attempts_left} left): ").strip().lower()
		if guess_text == "q":
			print(f"The number was {secret_number}.")
			return
		if not guess_text.isdigit():
			print("Enter a whole number from 1 to 100, or q to quit.")
			continue

		guess = int(guess_text)
		if not 1 <= guess <= 100:
			print("Your guess must be between 1 and 100.")
			continue

		attempts_left -= 1
		if guess == secret_number:
			print(f"You got it! The number was {secret_number}.")
			return
		if guess < secret_number:
			print("Too low!")
		else:
			print("Too high!")

	print(f"Out of guesses! The number was {secret_number}.")


def main() -> None:
	print("NUMBER GUESSING GAME")
	while True:
		play_round()
		while True:
			play_again = input("\nPlay again? (y/n): ").strip().lower()
			if play_again in ("y", "n"):
				break
			print("Enter y to play again or n to quit.")
		if play_again == "n":
			print("Thanks for playing!")
			return


if __name__ == "__main__":
	main()
