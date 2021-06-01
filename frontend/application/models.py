from application import db

class Marine(db.model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)