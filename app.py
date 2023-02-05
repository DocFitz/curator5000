#start with a simple monoapplciation then eventually move to a microservice type strcuture.
#here we are going to take ideas submitted from users and have them viewable with a lot of filters for users
#ideas will be marked as "viewed" for the users, they can also move to "selected"
#ideas that are selected 

#youtube api to verify that you are who you say you are creator
#authentication method (oauth login?)

from flask import Flask, abort, render_template
from markupsafe import escape
import datetime


app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/login/')
def about():
    return render_template('login.html')

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)
'''
@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)
        '''