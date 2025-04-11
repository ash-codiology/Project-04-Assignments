import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# Generate a random number
secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = input("Enter your guess (or type 'exit' to quit): ")

    if guess.lower() == 'exit':
        print(f"The secret number was {secret_number}. Better luck next time!")
        break

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again. ⬆️")
    elif guess > secret_number:
        print("Too high! Try again. ⬇️")
    else:
        print(f"MUBARAK HOOOO! You guessed the number {secret_number} in {attempts} attempts! ")
        break

print("Thanks for playing! 😄")
