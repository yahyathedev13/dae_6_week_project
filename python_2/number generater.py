import random
from pathlib import Path


BEST_SCORE_FILE = Path(__file__).with_name("best_guess_score.txt")


def load_best_score() -> int | None:
	stats_file = None
	try:
		stats_file = BEST_SCORE_FILE.open("r", encoding="utf-8")
		best_score = int(stats_file.read().strip())
	except FileNotFoundError:
		return None
	except (OSError, ValueError) as error:
		print(f"Couldn't read the saved best score: {error}")
		return None
	else:
		if 1 <= best_score <= 7:
			print(f"Best score so far: {best_score} guesses.")
			return best_score
		print("Saved score is invalid; starting a new record.")
		return None
	finally:
		if stats_file is not None:
			stats_file.close()


def save_best_score(best_score: int) -> None:
	stats_file = None
	try:
		stats_file = BEST_SCORE_FILE.open("w", encoding="utf-8")
		stats_file.write(str(best_score))
	except OSError as error:
		print(f"Couldn't save the best score: {error}")
	else:
		print("New best score saved.")
	finally:
		if stats_file is not None:
			stats_file.close()


def show_guess_history(guesses: list[int]) -> None:
	if guesses:
		print("Your guesses:", end=" ")
		for guess in guesses:
			print(guess, end=" ")
		print()
	else:
		print("You didn't make any guesses this round.")


def play_round() -> int | None:
	secret_number = random.randint(1, 100)
	attempts_left = 7
	guess_history = []

	print("\nI'm thinking of a number between 1 and 100.")
	print(f"You have {attempts_left} guesses. Type q to quit this round.")

	while attempts_left > 0:
		guess_text = input(f"\nYour guess ({attempts_left} left): ").strip().lower()
		if guess_text == "q":
			print(f"The number was {secret_number}.")
			show_guess_history(guess_history)
			return None
		if not guess_text.isdigit():
			print("Enter a whole number from 1 to 100, or q to quit.")
			continue

		guess = int(guess_text)
		if not 1 <= guess <= 100:
			print("Your guess must be between 1 and 100.")
			continue

		attempts_left -= 1
		guess_history.append(guess)
		if guess == secret_number:
			print(f"You got it! The number was {secret_number}.")
			show_guess_history(guess_history)
			return len(guess_history)
		if guess < secret_number:
			print("Too low!")
		else:
			print("Too high!")

	print(f"Out of guesses! The number was {secret_number}.")
	show_guess_history(guess_history)
	return None


def main() -> None:
	print("NUMBER GUESSING GAME")
	best_score = load_best_score()
	while True:
		round_score = play_round()
		if round_score is not None:
			if best_score is None or round_score < best_score:
				best_score = round_score
				save_best_score(best_score)
			else:
				print(f"Your best score is still {best_score} guesses.")
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
