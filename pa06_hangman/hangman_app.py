"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random
import string
wordlist=["cat", "dog", "elephant", "frog", "deer", "bird", "wolf", "lion", "mice", "dolphin", "fox"]
def generate_random_word(wordlist):
    word=random.choice(wordlist)
    while "-" in word or ' ' in word:
        word=random.choice(wordlist)
        
    return word


def play_hangman():
    want_to_play = True

    while (want_to_play):
        word = list(generate_random_word(wordlist).upper())
        word_letter = set(word)
        guessed_letter = set()
        guesses_left = 6

        print("- "*len(word))
        letter = input("pick a letter ")
        letter = letter.upper()

        done = False
        while not done:
            if letter not in word:
                guessed_letter.add(letter)
                print("this letter is not in the word")
                guesses_left = guesses_left-1
                print("you have", guesses_left, "guesses left")
            elif letter in guessed_letter:
                guesses_left=guesses_left-1
                print("you already guessed that letter")
                print("you have", guesses_left, "guesses left")
            else:
                guessed_letter.add(letter)
                word_letter.remove(letter) 
                print("this letter is in the word")
                print("you have", guesses_left, "guesses left")

            if len(word_letter)==0: 
                done=True
                print("you won!")
            elif guesses_left==0: 
                done=True
                print("you lost!")
            else:
                currentword = print_word(word, word_letter)
                print(' '.join(currentword))
                letter = input("please put another letter ")
                letter=letter.upper()
                
        want_to_play = input("do you want to play another game? Enter True or False ")
        if want_to_play.upper() == 'TRUE':
            want_to_play = True
        else:
            want_to_play = False
        
        
def print_word(word, word_letter):
    output = []
    for letter in word:
        if letter in word_letter:
            output.append('-')
        else:
            output.append(letter)
    return output

if __name__ == '__main__':
    play_hangman()
