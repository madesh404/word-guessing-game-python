import os
print("Working directory:", os.getcwd())

with open("5-letter-words.txt", "r") as file:
    WORDS = [w.strip().lower() for w in file.readlines()]
          
import random
word = random.choice(WORDS)
guessedWord = ['_'] * len(word)
attempts = 6

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
                print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break 

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)

