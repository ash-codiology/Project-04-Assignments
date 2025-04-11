import random

def hangman_game():
    words = ["computer", "elephant", "butterfly", "language", "mountain", "umbrella", "keyboard", "calendar", "airplane", "building"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 7

    print("Welcome to the Hangman Game!")
    print(f"The secret word has {len(word)} letters.")
    print("Word to guess: " + " ".join(["_" for _ in word]))
    print(f"You have {attempts} attempts to guess it.\n")

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess. '{guess}' is not in the word. Attempts left: {attempts}")

        current_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word to guess: " + " ".join(current_word) + "\n")

        if "_" not in current_word:
            print(f"Congratulations! You guessed the word: '{word}'")
            break

    if attempts == 0:
        print(f"Game over. The correct word was '{word}'. Better luck next time!")

    print("\nGame created By Ashfa Shakeel.")


hangman_game()
