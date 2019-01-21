import string

user_word = input("Enter a word you'd like to play with: ")
secret_word = list(user_word.lower())
hangman_word = list(len(user_word) * '_')
guesses = 0
game_Over = False
limit = int(len(user_word))
library = list(string.ascii_uppercase)

while not game_Over:
    changes = 0
    if guesses == limit:
        print("You lose! Game Over!")
        game_Over = True
        break
    elif secret_word == hangman_word:
        print("You win! Good Job!")
        game_Over = True
        break
    for i, item in enumerate(library):
        if (i + 1) % 13 == 0:
            print(item)
        else:
            print(item, end=' ')
    user_guess = input("Enter a letter you'd like to guess: ").lower()
    alpha_check = user_guess.isalpha()
    while user_guess.upper() not in library or alpha_check is False:
            user_guess = input("Enter a letter you'd like to guess (no repeats or non-alpha's allowed): ").lower()
            alpha_check = user_guess.isalpha()
    for index, letter in enumerate(library):
        if user_guess.upper() == library[index]:
            library.pop(index)
            library.insert(index - 1, "_")
    for index2, letter2 in enumerate(secret_word):
        secret_word_letter = letter2
        if secret_word_letter == user_guess:
            hangman_word[index2] = user_guess
            changes += 1
            continue
    print("".join(hangman_word))
    if changes == 0:
        print("You guessed wrong! Try again!")
        guesses += 1
