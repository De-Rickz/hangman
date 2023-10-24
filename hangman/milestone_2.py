import random

word_list = ['grapes','apple','apple','pineapple','banana']

def random_choice(word_list):
    word = random.choice(word_list)
    print(word)


random_choice(word_list)

guess = input("Enter a single letter")

if len(guess) == 1 & guess.isalpha():
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")