import random

def rock_paper_scissors():
    print(" Welcome to Ashfa's Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()

        if user_choice == 'exit':
            print("Thanks for playing! ")
            break

        if user_choice not in options:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie! 🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        print("\n--- Next Round ---\n")


rock_paper_scissors()
