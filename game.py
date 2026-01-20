import random

def start_game():
    # 1. Computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("--- WELCOME TO THE GUESSING GAME ---")
    print("I am thinking of a number between 1 and 100.")
    
    # 2. Start the loop
    while True:
        try:
            # Get user input
            user_guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # 3. Check the guess
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 CORRECT! You won in {attempts} attempts.")
                break # Exit the loop
                
        except ValueError:
            print("Please enter a valid number.")

# Run the game
start_game()