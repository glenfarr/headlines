from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_news():
    return """<h1>no news is good news!</h1>"""


if __name__ == '__main__':
    app.run(debug=True)