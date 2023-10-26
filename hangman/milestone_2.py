import random

favorite_fruits = ["apple", "banana", "strawberry", "kiwi", "mango"]
word_list = favorite_fruits

word = random.choice(word_list)

guess = input("Enter a single letter: ")

# Task 4: Check that the input is a single character
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!"
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input."
    print("Oops! That is not a valid input.")


