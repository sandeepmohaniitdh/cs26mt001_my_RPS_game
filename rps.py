def greet():
    print("Welcome to Rock Paper Scissors!")

def explain_rules():
    print("Rules: each player picks rock, paper, or scissors.")
    print("Rock beats scissors, scissors beats paper, paper beats rock.")
    print("Same choice is a tie.\n")

def main():
    greet()
    explain_rules()

if __name__ == "__main__":
    main()