import random
word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
print("The choosen word is:" + choosen_word)

# TOOD-1: CREATE A "placeholder" wth the same number of letters as the choosen word and display it to the user.

guess = input("Guess a letter:").lower()

#TODO-2 : create a "display that puts the guessed letter in the correct position and prints it out.