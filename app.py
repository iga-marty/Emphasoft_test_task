import os
import multiprocessing as mp
from flask import Flask, render_template
from flask_apscheduler import APScheduler


from random import randint
from time import sleep

from dotenv import load_dotenv
from celery import Celery


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!'

# # Celery configuration
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)


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

# @celery.on_after_configure.connect
# def setup_periodic_task(sender, **kwargs):
#     sender.add_periodic_task(10.0, creating_random_value.s())


def get_app():
    return app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home_page(arg):
    return str(arg)


@app.route('/git-webhook')
def git_webhook():
    pass


def random_value_fabrication():
    number = randint(1, 999)
    print(number)


if __name__ == '__main__':
    app.run(debug=True)



scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(id='test-job', func=random_value_fabrication, trigger='interval', seconds=5)

