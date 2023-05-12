
#importing the random module to generate random words for the game
import random

#importing string module to access string-related opreations
import string


#defining a function this will select a random word from the list below
def get_random_word():
    words = ['tosser', 'cheers', 'winner', 'yousuck', 'drake', 'spiderman', 'zombies']
    return random.choice(words)

def play_hangman():
    word = get_random_word()
    guessed_letters = []
    attempts = 6

    print("welcome to your doom with Hangman")

    while True:
        print("\nAttempts Left before doom:", attempts)
        print("failed Letters:", guessed_letters)
        display_word(word, guessed_letters)
        
        if is_word_guessed(word, guessed_letters):
            print("\nCongratulations! You guessed the word and prevented your doom:", word)
            break
        
        if attempts == 0:
            print("\nGame Over! You're officially doomed. The word was:", word)
            break
        
        guess = get_valid_letter(guessed_letters)
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Nope! That letter is not in the word, one guess closer to your doom.")

#define a dunction that will display the partially guessed word to the player

def display_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def get_valid_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess not in string.ascii_lowercase:
            print("Please enter a valid letter.")
        else:
            return guess

if __name__ == '__main__':
    play_hangman()
