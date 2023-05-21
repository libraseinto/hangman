# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

> This is the hangman project. The main goal is to build teh hangman game. If you are unfamiliar with it please visit the following link https://en.wikipedia.org/wiki/Hangman_(game)
> I will use python to write the code for this game. I will use tools like if/else statements, for loops, functions and OOP.The final product will be uploaded to GitHub

- The first milestone creates the list of words that I will use for the game. The list consist of five of my favourite fruits.
- After creating the list, it picks a word from that list at random using the random module and the method choice().
- Finally, it asks the user to input a letter to start guessing the word and checks that the user inputed a letter that is in the alphabet and not a number or a symbol.
- The code is below:
> '''import random
>
> word_list = ["mango", "papaya", "tangerine", "raspberry", "pineapple"]
> print(word_list)
> 
> word = random.choice(word_list)
> print(word)
>
> guess = input("Please input a letter: ")
> if len(guess) == 1 and guess.isalpha():
>    print("Good guess!")
> else:
>    print("Oops! That is not a valid input.")
>'''


