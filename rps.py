import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def greet():
    print("Welcome to Rock Paper Scissors!")

def explain_rules():
    print("Rules: each player picks rock, paper, or scissors.")
    print("Rock beats scissors, scissors beats paper, paper beats rock.")
    print("Same choice is a tie.\n")

def play_round():
    player = input("Enter your choice (rock, paper, scissors): ").strip()
    if player not in CHOICES:
        print("Invalid choice. Please type rock, paper, or scissors.")
        return None
    computer = random.choice(CHOICES)
    print(f"Computer chose: {computer}")
    if player == computer:
        return "tie"
    elif BEATS[player] == computer:
        return "player"
    else:
        return "computer"

def main():
    greet()
    explain_rules()
    result = play_round()
    while result == "tie" or result is None:
        if result == "tie":
            print("It's a tie! Rematch...\n")
        result = play_round()
    if result == "player":
        print("You win!")
    elif result == "computer":
        print("Computer wins!")

if __name__ == "__main__":
    main()