from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
 
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(120), unique=True)
    image = db.Column(db.String(200), unique=True)
    alt = db.Column(db.String(50), unique=True)

    def __init__(self, id=None, title=None, content=None, image=None, alt=None):
        self.id = id
        self.title = title
        self.content = content
        self.image = image
        self.alt = alt