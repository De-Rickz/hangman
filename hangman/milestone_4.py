import random

class Hangman:


    def __init__(self,word_list = ['grapes','apple','strawberry','pineapple','banana'], num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ["_"] * self.num_letters
        self.list_of_guesses = []

    
    def check_guess(self,guess):
        guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(letter)] = letter
            self.num_letters -= 1
        else:
            self.num_lives-= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left")
        
    
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter")

            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)   
                
        if self.num_lives == 0:
            print(f"Game over! The word was {self.word}.")
        else:
            print(f"Congratulations! You guessed the word {self.word}.")


if __name__ == "__main__":
    game = Hangman(['grapes', 'apple', 'pineapple','strawberry', 'banana'])
    game.ask_for_input()    
