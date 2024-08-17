import os

from random import randint

from flask import Flask, render_template
from flask_apscheduler import APScheduler
from dotenv import load_dotenv


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


def get_app():
    return app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home_page():
    return str(app.config.get('PASSED_VALUE'))


@app.route('/git-webhook')
def git_webhook():
    pass


def passed_value_fabrication():
    value = randint(1, 999)
    app.config['PASSED_VALUE'] = value
    print(value)



if __name__ == '__main__':
    app.run(debug=True)


passed_value_fabrication()

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(id='test-job', func=passed_value_fabrication, trigger='interval', seconds=5)

