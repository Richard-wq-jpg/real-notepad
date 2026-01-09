from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "I am alive"

@app.route("/get-notes")
def get_notes():
    return [
        {
            "title": "My first note",
            "body": "This is the body"
        },
        {
            "title": "My second note",
            "body": "This is the second body"
        },
    ]



if __name__ == "__main__":
    app.run(debug=True)

### Pythonanywhere, heroku, aws beanstalk