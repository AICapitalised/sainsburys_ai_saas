from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sainsburys_ai_saas.db'
db = SQLAlchemy(app)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    performance_score = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Supplier {self.name}>'
