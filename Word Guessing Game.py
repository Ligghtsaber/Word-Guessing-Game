import random

while True:
    word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
    word = random.choice(word_bank)
    guessedWord = ['_'] * len(word)
    attempts = 3

    print("\nNew Game Started! 🎉")

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
            print('\nYou have run out of attempts! The word was: ' + word)

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break

