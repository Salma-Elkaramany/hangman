import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                self.end_game()
    
    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1
    
    def end_game(self):
        if self.num_letters == 0:
            print(f"Congratulations! You guessed the word: {self.word}")
        else:
            print(f"Game over! You ran out of lives. The word was: {self.word}")
    
    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ")
            if self.is_valid_guess(guess):
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            else:
                print("Invalid input. Please enter a single alphabetical character.")
    
    def is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

# Example usage
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    hangman_game = Hangman(word_list)
    hangman_game.ask_for_input()