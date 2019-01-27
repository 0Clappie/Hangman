import string

user_word = input("Enter a word you'd like to play with: ")
secret_word = list(user_word.lower())
hangman_word = list(len(user_word) * '_')
guesses = 0


def changes_reset():
    changes = 0


limit = int(len(user_word))


def game_over_check():
    if guesses == limit:
        print("You lose! Game Over!")
        game_over = True
    elif secret_word == hangman_word:
        print("You win! Good Job!")
        game_over = True
    else:
        game_over = False
    return game_over


library = list(string.ascii_uppercase)


def print_library():
    for i, item in enumerate(library):
        if (i + 1) % 13 == 0:
            print(item)
        else:
            print(item, end=' ')


def user_guess_check():
    user_guess = input("Enter a letter you'd like to guess: ").lower()
    alpha_check = user_guess.isalpha()
    length_check = len(user_guess)
    while user_guess.upper() not in library or alpha_check is False or length_check != 1:
        user_guess = input("Enter a letter you'd like to guess "
                           "(no multi-chars, repeats or non-alpha's allowed): ").lower()
        alpha_check = user_guess.isalpha()
        length_check = len(user_guess)
    return user_guess


def library_alteration(user_guess):
    for index, letter in enumerate(library):
        if user_guess.upper() == library[index]:
            library.remove(user_guess.upper())
            library.insert(index, "_")


def scan_through_hangman_word(user_guess, changes):
    for index2, letter2 in enumerate(secret_word):
        secret_word_letter = letter2
        if secret_word_letter == user_guess:
            hangman_word[index2] = user_guess
            changes += 1
            continue
    return hangman_word, changes


def print_hangman_word_after_guess():
    return print("".join(hangman_word))


def guess_check(changes, guesses):
    if changes == 0:
        print("You guessed wrong! Try again!")
        guesses += 1
    return guesses


while game_over_check() is not True:
    changes_reset()
    print_library()
    user_guess_interim = user_guess_check()
    library_alteration(user_guess_interim)
    word_n_changes = list(scan_through_hangman_word(user_guess_interim, 0))
    print_hangman_word_after_guess()
    guess_check(word_n_changes[1], 0)
