import random
from words import words #from https://www.randomlists.com/data/words.json
# print(words) prints all words from words.property()
import string 

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guess
    lives = 6
    
    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        print('You have' , lives, 'lives left and used these letter: ', ''.join(used_letters))

        #what current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ''.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life
                print('Letter is not in word.')
        elif user_letter in word_letters:
            print('You have already used that character, Please try again.')
        else:
            print('Invalid try again')

    if lives == 0:
        print("You lost  the word was ", word)
    else:
        print('You guessed the word', word, '!!')
hangman()