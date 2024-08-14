import random

def play_game():
    Target = random.randint(1, 100)
    attempts = 0

    print("\n-------------------- Let's Play --------------------")
    print("Guess the number I'm thinking of between 1 and 100!")
    print("Type 'quit' at any time to exit the game.")
    
    while True:
        UserChoice = input("Enter your guess: ").strip().lower()
        
        if UserChoice == 'quit':
            print("You chose to quit the game. Thanks for playing!")
            break
        
        try:
            UserChoice = int(UserChoice)
            attempts += 1
            
            if UserChoice < 1 or UserChoice > 100:
                print("Please enter a number between 1 and 100.")
            elif UserChoice == Target:
                print(f"Success: Correct Guess!! It took you {attempts} attempts.")
                break
            elif UserChoice < Target:
                print("Too low! Try guessing a higher number.")
            else:
                print("Too high! Try guessing a lower number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("-------------------- GAME OVER --------------------")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    main()
