from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sainsburys_ai_saas.db'
db = SQLAlchemy(app)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    performance_score = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Supplier {self.name}>'

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Sainsbury's AI SaaS!"})

@app.route('/add_sample_data')
def add_sample_data():
    sample_supplier = Supplier(name='Sample Supplier', performance_score=85.5)
    db.session.add(sample_supplier)
    db.session.commit()
    return jsonify({"message": "Sample data added!"})

@app.route('/suppliers')
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([{"id": s.id, "name": s.name, "performance_score": s.performance_score} for s in suppliers])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

@app.route('/add_sample_data')
def add_sample_data():
    sample_supplier = Supplier(name='Sample Supplier', performance_score=85.5)
    db.session.add(sample_supplier)
    db.session.commit()
    return jsonify({"message": "Sample data added!"})

@app.route('/suppliers')
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([{"id": s.id, "name": s.name, "performance_score": s.performance_score} for s in suppliers])
