from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/login")
def login():
    print(request)
    return "login!!"


if __name__ == '__main__':
    app.run(debug=True)
