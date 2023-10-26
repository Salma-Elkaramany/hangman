# Defines the function to check the guess
def check_guess(guess, secret_word):
    # Convert the guess into lower case.
    guess = guess.lower()
    
    # Check if the guess is in the word.
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Defines the function to ask for input
def ask_for_input(secret_word):
    # Move the code for asking the user to guess into this function block.
    while True:
        guess = input("Guess a letter: ")
        # Call the check_guess function to check the guess.
        check_guess(guess, secret_word)
        if guess in secret_word:
            break

# Secret word (you can replace this with your actual secret word)
secret_word = "apple"

# Call the ask_for_input function to test your code.
ask_for_input(secret_word)