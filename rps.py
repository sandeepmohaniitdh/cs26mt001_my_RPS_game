#!/usr/bin/env python3
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
        print("It's a tie!")
    elif BEATS[player] == computer:
        print("You win!")
    else:
        print("Computer wins!")

def main():
    greet()
    explain_rules()
    play_round()

if __name__ == "__main__":
    main()