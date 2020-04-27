import random
import string
wordlist=["cat", "dog", "elephant", "frog", "deer", "bird", "wolf", "lion", "mice", "dolphin", "fox"]
def generate_random_word(wordlist):
    word=random.choice(wordlist)
    while "-" in word or ' ' in word:
        word=random.choice(wordlist)
        
    return word

def play_hangman(word, letters):
    word = list(word.upper())
    word_letter = set(word)
    guessed_letter = set()
    guesses_left = 6
    done = False
    data = {
        'message': '',
        'print_letter': '',
        'done': False
    }

    for letter in letters:
        letter = letter.upper()
        if letter not in word:
            guessed_letter.add(letter)
            guesses_left = guesses_left-1
            data['message'] = "this letter is not in the word"
        elif letter in guessed_letter:
            guesses_left=guesses_left-1
            data['message'] = "you already guessed that letter"
        else:
            guessed_letter.add(letter)
            word_letter.remove(letter)
            data['message'] = "this letter is in the word"

        data['message'] += "<br>you have " + str(guesses_left) + " guesses left"
        currentword = print_word(word, word_letter)
        data['print_letter'] = ''.join(currentword)

        if len(word_letter)==0: 
            done=True
            data['message'] = "you won!"
        elif guesses_left==0: 
            done=True
            data['message'] = "you lost!"

    data['done'] = done
    return data  
        
def print_word(word, word_letter):
    output = []
    for letter in word:
        if letter in word_letter:
            output.append('-')
        else:
            output.append(letter)
    return output

import json
from flask import Flask,request,render_template,redirect,jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hangman():
    if request.method =='POST':
        data = request.get_data()
        print(request.form)
        data = json.loads(data)

        flag = data['play']
        if flag == 0:
            print("Begin")
            word = generate_random_word(wordlist)
            print(word)
            output = {'word': word}
        elif flag == 1:
            word = data['word']
            letters = data['guess_letter']
            output = play_hangman(word, letters)
        else:
            output = {}
        return jsonify(output)
    else:
        return render_template('hangman.html')

@app.route('/')
@app.route('/bio')
def main():
 return render_template('bio.html')

if __name__ == '__main__':
    app.run(debug=True)
