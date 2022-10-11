from src.utils.initdb import db

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<pname %r>' % self.pname

