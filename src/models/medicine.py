from src.utils.initdb import db

class Medicine(db.Model):
    name = db.Column(db.String(1200), unique=True, nullable=False)
    description = db.Column(db.String(1200), nullable=False)
    url = db.Column(db.String(1200), nullable=False, primary_key=True)
    use = db.Column(db.String(1200), nullable=False)
    side_effect = db.Column(db.String(1200), nullable=False)

    # constructor
    def __init__(self, name, description, url, use, side_effect):
        self.name = name
        self.description = description
        self.url = url
        self.use = use
        self.side_effect = side_effect


        
        
