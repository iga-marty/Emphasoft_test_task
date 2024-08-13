import os
from flask import Flask, make_response, send_file, render_template


app = Flask(__name__)

def get_app():
    return app



@app.route('/')
def index():
    return render_template('index.html')













if __name__ == '__main__':
    app.run(debug=True)