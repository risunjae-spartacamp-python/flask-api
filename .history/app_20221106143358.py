from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data= {
        
    }
    return "Hello API"


if __name__ == "__main__":
    app.run(debug=True)
