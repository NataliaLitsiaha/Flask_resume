from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///work.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Text, nullable=False)
    duty = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Work %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/works')
def works():
    work_experience = Work.query.order_by(Work.id).all()
    return render_template("works.html", work_experience=work_experience)


@app.route('/skills')
def skills():
    return render_template("skills.html")


if __name__ == '__main__':
    app.run(debug=True)

