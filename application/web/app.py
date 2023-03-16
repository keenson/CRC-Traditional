import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env file into environment




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =  'sqlite:///visitors.db'


# Secrete Key!
app.config["SECRET_KEY"] = "my super secret key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize The Database
db = SQLAlchemy(app)


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self):
        self.count = 0

@app.route("/")
def hello():
    v = Visit.query.first()
    if not v:
        v = Visit()
        # v.count += 1
        db.session.add(v)
    v.count += 1
    db.session.commit()
    return render_template('index.html', counter=v.count)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

