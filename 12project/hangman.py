import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word and ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter=set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter= set()
    lives = 10

    while len(word_letter) > 0 and lives > 0 :

        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have',lives , ' left. You used this letter ', ' '.join(used_letter))

        # what current word is (ie W - R D)
        word_list= [ letter if letter in used_letter else '-' for letter in word ]
        print('current : ', ' '.join(word_list))

        user_letter = input("\nGuess a letter :").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives = lives -1
                print('Letter is not in the world')

        elif user_letter in used_letter:
            print('\nYou have already used that letter. Guess another letter.')
        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print('You are Dead , sorry the word is ',word )
    else:
        print('\nYou guessed the word: ',word ,'!!')


hangman()