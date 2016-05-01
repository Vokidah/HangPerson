from flask import Flask, request, render_template, redirect, url_for
from hang_person_game import HangPersonGame
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/new', methods=['GET', 'POST'])
def new_game():
    if request.method == 'GET':
        return render_template('new.html')
    else:
        global hang_person_game
        hang_person_game = HangPersonGame(get_random_word())
        return redirect(url_for('show'))


@app.route('/show', methods=['GET', 'POST'])
def show():
    global hang_person_game
    if request.method == 'GET':
        return render_template('show.html', guesses=hang_person_game.word_with_guesses())
    else:
        if int(request.form['guess']) == 0:
            hang_person_game.guess(request.form['letter'])
            if hang_person_game.check_win_or_lose() == 2:
                return redirect(url_for('show'))
            elif hang_person_game.check_win_or_lose() == 1:
                return redirect(url_for('win'))
            else:
                return redirect(url_for('lose'))
        else:
            return redirect(url_for('new_game'))


@app.route('/win', methods=['GET', 'POST'])
def win():
    global hang_person_game
    if request.method == 'GET':
        return render_template('win.html', word=hang_person_game.word)
    else:
        return redirect(url_for('new_game'))


@app.route('/lose', methods=['GET', 'POST'])
def lose():
    global hang_person_game
    if request.method == 'GET':
        return render_template('lose.html', word=hang_person_game.word)
    else:
        return redirect(url_for('new_game'))


def get_random_word():
    return requests.post('http://watchout4snakes.com/wo4snakes/Random/RandomWord').text


if __name__ == '__main__':
    hang_person_game = None
    app.run(debug=True)
