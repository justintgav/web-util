from flask import Flask

app = Flask(__name__)


@app.route("/app", methods=['POST','GET'])
def home():
    return "asdf"
