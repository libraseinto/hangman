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
