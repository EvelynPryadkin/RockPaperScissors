import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    ties = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in options:
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(options)
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
            ties += 1
        elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print("\nScore:")
        print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")

        while True:
            play_again = input("Play again? (yes/no): ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("\nFinal score:")
                print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
                print("Thank you for playing!")
                return
            else:
                print("Please input 'yes' or 'no'.")

play_game()





