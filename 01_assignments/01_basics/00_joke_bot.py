import random

PROMPT: str = "What do you want? (type 'joke' for a joke, or 'exit' to quit): "
JOKES: list = [
    " Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs.'",
    " Why do programmers prefer dark mode? Because the light attracts bugs!",
    " Why do Java developers wear glasses? Because they don’t see sharp!",
    " Debugging: Being the detective in a crime movie where you are also the murderer.",
    " A user interface is like a joke. If you have to explain it, it’s not that good."
]
SORRY: str = "Sorry, I only tell jokes. Please type 'joke'!"

def main():
    while True:
        user_input = input(PROMPT).strip().lower()
        
        if user_input == "exit":
            print("👋 Goodbye! Have a great day!")
            break
        elif "joke" in user_input:
            print(random.choice(JOKES))
        else:
            print(SORRY)

if __name__ == "__main__":
    main()
