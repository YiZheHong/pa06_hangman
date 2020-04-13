"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':" ",
		 'word_so_far':" ",
		 'done':False,
		 'word123':" ",
         'correct':" "}

def word(random_word, letter):
    positions = []
    start_at = -1
    while True:
        try:
            position = random_word.index(letter, start_at + 1)
        except ValueError:
            break
        else:
            positions.append(position)
            start_at = position

    return positions

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word()
	state['guesses'] = []
	guessed123= hangman_app.guess(state['word'])
	state['word_so_far'] = guessed123
	return render_template("start.html",state=state)


@app.route('/play',methods=['GET','POST'])
def hangman():
    global state
    if request.method == 'GET':
        return start()
    elif request.method == 'POST':
        letter = request.form['guess']
        if letter in state['guesses']:
            state['word123'] = 'You have already guessed this letter. Please try another one.'
        elif letter not in state['word']:
            state['guesses'] +=letter#
            state['word123'] = '"Sorry, this letter is not in the word. Please try again.'#tell user the letter is not in the word
        elif letter in state['word']:
            state['guesses'] += letter##add letter to guessed letters
            state['word123'] = 'Great, this letter is in the word'# check if letter has already been guessed

            for i in word(state['word'], letter):
                state['word_so_far'][i] = state['word'][i]
                state['correct'] += letter

            if len(state['word'])+1 == len(state['correct']):
                state['word123'] = 'You won! The word is '+ state['word']
        return render_template('play.html',state=state)

@app.route('/about')
def about():
	global state

	return render_template("about.html",state=state)

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
