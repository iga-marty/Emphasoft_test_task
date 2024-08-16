import os
import multiprocessing as mp
from flask import Flask, render_template

from random import randint
from time import sleep

from dotenv import load_dotenv
from celery import Celery


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH2_PROVIDERS'] = {
    'github': {
        'client_id': os.environ.get('GITHUB_CLIENT_ID'),
        'client_secret': os.environ.get('GITHUB_CLIENT_SECRET'),
        'authorize_url': 'https://github.com/login/oauth/authorize',
        'token_url': 'https://github.com/login/oauth/access_token',
        'userinfo': {
            'url': 'https://api.github.com/user/emails',
            'email': lambda json: json[0]['email'],
        },
        'scopes': ['user:email'],
    },
}


celery = Celery(app.name)

@celery.task
def creating_random_value():
    pass


def get_app():
    return app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/git-webhook')
def git_webhook():
    return str(number.value)


def random_value_fabrication():
    while True:
        with number.get_lock():
            number.value = randint(1, 999)
        sleep(5)


if __name__ == '__main__':
    # def start_app():
    #     return app.run(debug=True)


    mp.freeze_support()
    number = mp.Value('i', 0, lock=True)

    p_1 = mp.Process(target=app.run)
    p_2 = mp.Process(target=random_value_fabrication)

    p_1.start()
    p_2.start()
