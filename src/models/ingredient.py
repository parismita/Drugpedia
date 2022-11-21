from src.utils.initdb import db

class Ingredients(db.Model):
    name = db.Column(db.String(1200), unique=True, nullable=False)
    precautions = db.Column(db.String(1200), nullable=False)
    url = db.Column(db.String(1200), nullable=False, primary_key=True)
    use = db.Column(db.String(1200), nullable=False)
    side_effect = db.Column(db.String(1200), nullable=False)


    def __init__(self, name, precautions, url, use, side_effect):
        self.name = name
        self.precautions = precautions
        self.url = url
        self.use = use
        self.side_effect = side_effect
    
    def json(self):
        return {
            "name":self.name,
            "precautions":self.precautions,
            "url":self.url,
            "use":self.use,
            "side_effect":self.side_effect
        }


