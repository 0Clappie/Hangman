import string


def get_secret_word():
    """Ask for one playable word and return it in lowercase."""
    while True:
        secret_word = input("Enter a word you'd like to play with: ").strip().lower()
        if secret_word and all(letter in string.ascii_lowercase for letter in secret_word):
            return secret_word
        print("Please enter one word using only A-Z letters.")


def print_library(library):
    """Print the available letters in two rows."""
    for index, letter in enumerate(library, start=1):
        line_end = "\n" if index % 13 == 0 else " "
        print(letter, end=line_end)


def get_user_guess(library):
    """Return one available A-Z letter in lowercase."""
    while True:
        user_guess = input("Enter a letter you'd like to guess: ").strip().lower()

        if len(user_guess) != 1 or user_guess not in string.ascii_lowercase:
            print("Please enter exactly one A-Z letter.")
        elif user_guess.upper() not in library:
            print("You already guessed that letter. Try another one.")
        else:
            return user_guess


def mark_letter_used(library, user_guess):
    """Replace a guessed letter with an underscore in the letter library."""
    index = library.index(user_guess.upper())
    library[index] = "_"


def reveal_letter(secret_word, hangman_word, user_guess):
    """Reveal every match and return how many matches were found."""
    matches = 0
    for index, letter in enumerate(secret_word):
        if letter == user_guess:
            hangman_word[index] = user_guess
            matches += 1
    return matches


def get_game_result(secret_word, hangman_word, wrong_guesses, limit):
    """Return 'win', 'lose', or None while the game is still running."""
    if hangman_word == list(secret_word):
        return "win"
    if wrong_guesses >= limit:
        return "lose"
    return None


def main():
    secret_word = get_secret_word()
    hangman_word = ["_"] * len(secret_word)
    library = list(string.ascii_uppercase)
    wrong_guesses = 0
    limit = len(secret_word)

    print("".join(hangman_word))

    while True:
        print_library(library)
        user_guess = get_user_guess(library)
        mark_letter_used(library, user_guess)

        matches = reveal_letter(secret_word, hangman_word, user_guess)
        print("".join(hangman_word))

        if matches == 0:
            wrong_guesses += 1
            print(f"Wrong guess! {limit - wrong_guesses} wrong guesses remaining.")

        game_result = get_game_result(
            secret_word, hangman_word, wrong_guesses, limit
        )
        if game_result == "win":
            print("You win! Good job!")
            break
        if game_result == "lose":
            print(f"You lose! The word was '{secret_word}'.")
            break


if __name__ == "__main__":
    main()
