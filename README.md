# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

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

> ![Milestone_2](C:\Users\alexa\OneDrive\Desktop\Milestone_2.png)  

## Milestone 2

- Milestone 2 enhances the readability of the code by adding functions
- The first function check_guess, makes sure the word the user input as a guess is in the word and prints a message if it is, if not, prints another message letting him know that the letter is not in the word
- The other function ask_for_input, asks the user for input (to guess a letter), and checks that the guess is valid (i.e an alphabetic single character), if the guess is not valid, it prints a message to let the user know and keeps asking him until he inputs a valid character. This is achieved by the use of a while loop
- The code is below:


```
import random

word_list = ["mango", "papaya", "tangerine", "raspberry", "pineapple"]
print(word_list)

word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character")
```
## Milestone 3

- In milestone 3 I created the class Hangman to improve even more the readability of my code
- I named the class `Hangman`. Then I initialised the class with the funcion `__init__` with the following attributes: word_list, num_lives, word, word_guessed, num_letters, list_of_guesses
- I defined the functions in milestone 2 as methods inside the class
- The methond `check_guess` was redefined to check not only if the guess is in the word, but to also populate the list `word_guessed` and to reduce the number of lives by 1 if the guess is incorrect.

The code is below:
```
import random

# word_list = ["mango", "papaya", "tangerine", "raspberry", "pineapple"]

class Hangman:


    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(guess)] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried this letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
```
## Milestone 5

- In this milestone I created the final logic for the game.
- I created the function `play_game` to execute the full game. This function starts the class by creating an instance of it, passing a list of words and the initial number of lives
- The function `play_game` then calls the methods inside the class in a while loop to keep asking the user for input until they either guess the word or ran out ot lives
- The game is won by having more than 0 lives and reducing to 0 the attribute `num_letters` which contains the number of unique letters in the word to be guessed and everytime the user guess a word, -1 is taken from the attribute

The code is below:
```
import random

class Hangman:


    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(guess)] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried this letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

play_game(word_list = ["mango", "papaya", "tangerine", "raspberry", "pineapple"])
```

