import random

def game():
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock/paper/scissor): ").lower()
    while user not in choices:
        user = input("Invalid input. Enter your choice (rock/paper/scissor): ").lower()

    print(f"\nComputer chose {computer}, you chose {user}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissor":
            print("Rock smashes scissor! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissor cuts paper! You lose.")
    elif user == "scissor":
        if computer == "paper":
            print("Scissor cuts paper! You win!")
        else:
            print("Rock smashes scissor! You lose.")

if __name__ == "__main__":
    game()