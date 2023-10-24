import random

word_list = ['grapes','apple','apple','pineapple','banana']
def random_choice(word_list):
    word = random.choice(word_list)
    return word
    



def check_guess(guess):
    guess.lower()

    if guess in random_choice(word_list):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Enter a letter")

        if len(guess) == 1 & guess.isalpha():
            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)



ask_for_input()