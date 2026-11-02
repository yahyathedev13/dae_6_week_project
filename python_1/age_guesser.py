from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    options: tuple[str, ...]
    estimates: tuple[int, ...]
    weight: int = 1


QUESTIONS = (
    Question(
        "Which best describes your day-to-day life?",
        (
            "I'm in primary or middle school",
            "I'm in high school",
            "I'm studying at college or in training",
            "I work full time",
            "I'm retired or close to it",
        ),
        (11, 16, 21, 34, 68),
        weight=2,
    ),
    Question(
        "What was the first kind of music player you remember using?",
        (
            "A streaming app",
            "An MP3 player or iPod",
            "A portable CD player",
            "A cassette player or Walkman",
            "A record player",
        ),
        (17, 27, 36, 46, 58),
    ),
    Question(
        "Which internet experience feels most familiar from growing up?",
        (
            "The internet was always around",
            "Using Wi-Fi at home",
            "Getting online through broadband",
            "Dial-up and a phone line",
            "I mostly remember life before home internet",
        ),
        (17, 25, 34, 45, 60),
    ),
    Question(
        "When did you get your first phone of your own?",
        (
            "Before age 10",
            "Around ages 10-12",
            "Around ages 13-15",
            "At 16 or older",
            "I haven't had one of my own",
        ),
        (24, 28, 33, 40, 35),
    ),
)

LIFE_STAGE_AGE_RANGES = (
    (8, 14),
    (14, 18),
    (18, 35),
    (18, 67),
    (60, 100),
)


def ask_question(question: Question, number: int) -> int | None:
    print(f"\n{number}. {question.prompt}")
    for option_number, option in enumerate(question.options, start=1):
        print(f"  {option_number}. {option}")

    while True:
        answer = input("Choose 1-{} (or q to quit): ".format(len(question.options)).strip())
        if answer.lower() == "q":
            return None
        if answer.isdigit() and 1 <= int(answer) <= len(question.options):
            return int(answer) - 1
        print(f"Please enter a number from 1 to {len(question.options)}, or q to quit.")


def guess_age() -> int | None:
    weighted_total = 0
    total_weight = 0
    selected_age_range = None

    print("\nAGE GUESSER")
    print("Answer a few questions and I'll make a playful guess.")

    for number, question in enumerate(QUESTIONS, start=1):
        answer_index = ask_question(question, number)
        if answer_index is None:
            print("No problem. See you next time!")
            return None
        estimate = question.estimates[answer_index]
        weighted_total += estimate * question.weight
        total_weight += question.weight
        if number == 1:
            selected_age_range = LIFE_STAGE_AGE_RANGES[answer_index]

    guess = round(weighted_total / total_weight)
    if selected_age_range is not None:
        minimum_age, maximum_age = selected_age_range
        guess = max(minimum_age, min(guess, maximum_age))
    return guess


def main() -> None:
    while True:
        estimate = guess_age()
        if estimate is None:
            return

        print(f"\nMy guess: {estimate} years old!")
        print("Just for fun: these clues are rough and vary by person and region.")

        while True:
            answer = input("Was my guess right? (y/n): ").strip().lower()
            if answer in ("y", "n"):
                break
            print("Please enter y or n.")

        if answer == "n":
            while True:
                correct_age = input("What's your correct age? (0-130): ").strip()
                if correct_age.isdigit() and 0 <= int(correct_age) <= 130:
                    print(f"Thanks for the correction: {int(correct_age)} years old.")
                    return
                print("Please enter a whole number from 0 to 130.")

        print("Glad I got it right!")
        while True:
            play_again = input("Try again? (y/n): ").strip().lower()
            if play_again == "y":
                break
            if play_again == "n":
                print("Thanks for playing!")
                return
            print("Please enter y to try again or n to end.")


if __name__ == "__main__":
    main()
