#word_list = ["anaconda","bear","camel","dinosaur"]

import random
import os
from hangman_words import word_list


choosen_word = random.choice(word_list)
word_len = len(choosen_word)

lives = 6

from hangman_art import logo
print(logo)

#Testing code
print("Choosen word is "+choosen_word)

#create blanks
display = []
for _ in range(word_len):
    display += "_"
print(display)
end_of_game = False
while not end_of_game :
    guess = input("Guess a letter : ").lower()

    os.system('cls')

    if guess in display :
        print(f"You 've already guessed {guess}")
    
    #check guessed letter
    for position in range(word_len) :
        letter = choosen_word[position]
        if letter ==guess :
            display[position]=letter
    
    #check if user is wrong
    if guess not in choosen_word :
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0 :
            end_of_game = True
            print("\n------YOU LOSE------\n")
    print(display)
    #check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("\n------YOU WIN------\n")
        
    from hangman_art import stages
    print(stages[lives])