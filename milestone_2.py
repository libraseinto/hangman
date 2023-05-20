import random

word_list = ["mango", "papaya", "tangerine", "raspberry", "pineapple"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please input a letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")