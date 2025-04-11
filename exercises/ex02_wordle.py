"""My First Wordle"""

__author__: str = "730572401"


def contains_char(word: str, char: str) -> bool:
    """
    Checks if the given character is present in the word.
    Returns True if found, otherwise False.
    """
    assert len(char) == 1, f"len('{char}') is not 1"

    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


# Emoji constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """
    Returns a string of emoji codifying the guess result against the secret word.
    """
    assert len(guess) == len(secret), "Guess must be same length as secret"

    emoji_result: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        i += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    """
    Prompts the user for a guess of the expected length and returns it.
    """
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """
    The entry point of the program and main game loop.
    """
    turns: int = 1
    max_turns: int = 6
    won: bool = False

    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turns += 1

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
