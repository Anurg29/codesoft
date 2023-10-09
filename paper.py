import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    # Get user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Ensure the user's choice is valid
    if user_choice not in choices:
        print("Invalid choice. Please choose from rock, paper, or scissors.")
        return

    # Generate a random choice for the computer
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        print(f"It's a tie! Both chose {user_choice}.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")

# Main loop
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
