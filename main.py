import random

# Generate a random integer between 1 and 100
secret_number = random.randint(1, 100)

print("I've picked a number between 1 and 100. Try to guess it!")
# print(f"(Hint: The number is {secret_number})") # Let's remove or comment out the hint now

guesses_taken = 0 # Variable to count guesses

while True: # Main game loop
    # Get the player's guess (with validation)
    while True: # Inner loop for input validation
        try:
            guess_str = input("Enter your guess: ")
            guess = int(guess_str) # Convert the input string to an integer
            guesses_taken = guesses_taken + 1 # Increment guess counter
            break # Exit the inner loop if conversion was successful
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Compare the guess to the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        # Correct guess!
        print(f"Correct! You guessed the number {secret_number} in {guesses_taken} tries!")
        break # Exit the main game loop

# --- End of game ---