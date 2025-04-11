import random

def computer_guess():
    print("\n🤖 I'm going to guess your number between 1 and 10!")
    input("Think of a number between 1 and 10 and press Enter when you're ready...")

    low = 1
    high = 10
    attempts = 0

    while True:
        if low > high:
            print("⚠️ Oops! Something went wrong. Maybe you gave a wrong hint. 🤔")
            break

        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Hayeee mazeeee! I guessed your number in {attempts} attempts!")
            break
        else:
            print("Please respond with H (high), L (low), or C (correct).")

# Run only computer guess
computer_guess()
