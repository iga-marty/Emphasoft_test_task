import multiprocessing as mp
from flask import Flask, render_template

from random import randint
from time import sleep

app = Flask(__name__)


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
