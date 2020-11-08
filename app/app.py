import db
from datetime import datetime
from flask import Flask, request
import json 

app = Flask(__name__)
db_filename = "wastenot.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.db.init_app(app)
with app.app_context():
    db.db.create_all()

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

# Item routes
@app.route('/')
@app.route('/api/items/')
def get_all_items():
    data = [i.serialize() for i in db.Item.query.all()]
    sort = request.args.get('sort')
    if sort == "increasing":
        data = sorted(data, key=lambda k: k['expiry_date']) 
    elif sort == "decreasing":
        data = sorted(data, key=lambda k: k['expiry_date'], reverse = True) 
    return success_response(data)

@app.route('/api/runs/<int:run_id>/item/', methods=['POST'])
@app.route('/api/items/', methods=['POST'])
def create_item(run_id = None):
    body = json.loads(request.data)
    if body.get("name") is None: 
        return failure_response("Missing name")
    if body.get("expiry_date") is None: 
        return failure_response("Missing expiration date")
    if body.get("purchase_date") is None: 
        return failure_response("Missing purchase date")
    if body.get("category") is None:
        return failure_response("Missing category")
    elif body.get("category") != "pantry" and body.get("category") != "fridge" and body.get("category") != "freezer":
        return failure_response("Invalid category")
    new_item = db.Item(name=body.get("name"), purchase_date=body.get("purchase_date"), expiry_date=body.get("expiry_date"), notes=body.get("notes", ""), category=body.get("category"), run_id=run_id)
    db.session.add(new_item)
    db.session.commit()
    return success_response(new_item.serialize(), 201)

@app.route('/api/items/<int:item_id>/', methods=['POST'])
def update_item(item_id):
    item = db.Item.query.filter_by(id = item_id).first() 
    if item is None:
        return failure_response("Item not found")
    body = json.loads(request.data)
    item.name = body.get("name", item.name)
    item.notes = body.get("notes", item.notes)
    item.purchase_date = body.get("purchase_date", item.purchase_date)
    item.expiry_date = body.get("expiry_date", item.expiry_date)
    if body.get("category") is not None and body.get("category") != "pantry" and body.get("category") != "fridge" and body.get("category") != "freezer":
        return failure_response("Invalid category")
    item.category = body.get("category", item.category)
    db.session.commit()
    return success_response(item.serialize(), 201)

@app.route('/api/items/<int:item_id>/')
def get_item(item_id):
    item = db.Item.query.filter_by(id = item_id).first()
    if item is None:
        return failure_response("Item not found")
    return success_response(item.serialize())

@app.route('/api/items/filter/')
def get_items_by_category():
    body = json.loads(request.data)
    if body.get("category") != "pantry" and body.get("category") != "fridge" and body.get("category") != "freezer":
        return failure_response("Invalid category")
    items = [i.serialize() for i in db.Item.query.filter_by(category=body.get("category"))]
    sort = request.args.get('sort')
    if sort == "increasing":
        data = sorted(items, key=lambda k: k['expiry_date']) 
    elif sort == "decreasing":
        data = sorted(items, key=lambda k: k['expiry_date'], reverse = True) 
    return success_response(items)

@app.route('/api/items/<int:item_id>/', methods=['DELETE'])
def delete_item(item_id):
    item = db.Item.query.filter_by(id=item_id).first()
    if item is None:
        return failure_response("Item not found")
    db.session.delete(item)
    db.session.commit()
    return success_response(item.serialize())

# Grocery run routes
@app.route('/api/run/', methods=['POST'])
def create_run():
    body = json.loads(request.data)
    if body.get("date") is None: 
        return failure_response("Missing date")
    new_run = db.Run(date = body.get("date"))
    db.session.add(new_run)
    db.session.commit()
    return success_response(new_run.serialize(), 201)

@app.route('/api/runs/')
def get_runs():
    data = [r.serialize() for r in db.Run.query.all()]
    sort = request.args.get('sort')
    if sort == "increasing":
        data = sorted(data, key=lambda k: k['expiry_date']) 
    elif sort == "decreasing":
        data = sorted(data, key=lambda k: k['expiry_date'], reverse = True) 
    return success_response(data)

@app.route('/api/runs/<int:run_id>/')
def get_run(run_id):
    run = db.Run.query.filter_by(id = run_id).first()
    if run is None:
        return failure_response("Run not found")
    return success_response(run.serialize())

@app.route('/api/runs/<int:run_id>/', methods=['POST'])
def update_run(run_id):
    run = db.Run.query.filter_by(id = run_id).first() 
    if run is None:
        return failure_response("Run not found")
    body = json.loads(request.data)
    run.date = body.get("date", run.date)
    db.session.commit()
    return success_response(run.serialize(), 201)

@app.route('/api/runs/<int:run_id>/', methods=['DELETE'])
def delete_run(run_id):
    run = db.Run.query.filter_by(id=run_id).first()
    if run is None:
        return failure_response("Run not found")
    db.session.delete(run)
    db.session.commit()
    return success_response(run.serialize())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)