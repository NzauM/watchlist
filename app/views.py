from flask import render_template
from app import app

@app.route('/')
def index():

    message = 'Hello World'
    return render_template('index.html',message  = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id = movie_id)

def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to the best movie review website online'
    return render_template('index.html',title = title)