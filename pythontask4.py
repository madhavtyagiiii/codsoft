import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    while True:
        print("\nChoose one: rock, paper, scissors")
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("🔁 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ You lost this round.")
            computer_score += 1

        print(f"📊 Score – You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Play another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing!")
            break

# Run the game
play_game()