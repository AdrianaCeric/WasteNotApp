from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here
class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    expiry_date = db.Column(db.Integer, nullable = False)
    purchase_date = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.String, nullable = False)
    category = db.Column(db.String, nullable = False)
    run_id = db.Column(db.Integer, db.ForeignKey('run.id'))

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.expiry_date = kwargs.get('expiry_date')
        self.purchase_date = kwargs.get('purchase_date')
        self.notes = kwargs.get('notes')
        self.category = kwargs.get('category')
        self.run_id = kwargs.get('run_id')

    def serialize(self):
        return {
            "id": self.id,
            "purchase_date": self.purchase_date,
            "name": self.name,
            "expiry_date": self.expiry_date,
            "notes": self.notes,
            "category": self.category
        }      

class Run(db.Model):
    __tablename__ = "run"
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Integer, nullable = False)
    items = db.relationship("Item", cascade = "delete")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.date = kwargs.get('date')

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "items": [i.serialize() for i in self.items]
        }  