import random

def print_intro():
    print("Welcome to Rock, Paper, Scissors game!")
    print("Rules:")
    print("Rock beats Scissors (Rock crushes Scissors)")
    print("Scissors beats Paper (Scissors cut Paper)")
    print("Paper beats Rock (Paper covers Rock)")
    print("Let's play!")

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors, or quit): ").lower()
    while choice not in ["rock", "paper", "scissors", "quit"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors, or quit): ").lower()
    return choice


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)



def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"
    


def main():
    print_intro()
    user_score = 0
    computer_score = 0
    draw_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            break

        computer_choice = get_computer_choice()
        if user_choice == "quit":
            break

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        winner = determine_winner(user_choice, computer_choice)
        if winner == "draw":
            print("It's a draw!")
            draw_score += 1
        elif winner == "user":
            print("Congratulations! You win!")
            user_score += 1
        else:
            print("Computer wins. Better luck next time!")
            computer_score += 1

        print("Score: You -", user_score, "| Computer -", computer_score, "| Draws -", draw_score)

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
