from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data= {
        message
    }
    return "Hello API"


if __name__ == "__main__":
    app.run(debug=True)
