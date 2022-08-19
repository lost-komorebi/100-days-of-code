from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    all_ids = db.session.query(Cafe.id).all()  # get specific column from db
    cafe_id = choice(all_ids)[0]  # get value from a tuple
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    # obj.__dict__ can convert a SQLAlchemy  object to a Python dict.
    # remove key _sa_instance_state
    cafe.__dict__.pop("_sa_instance_state", None)
    return jsonify({"cafe": cafe.__dict__})


@app.route('/get-all', methods=["GET"])
def get_all():
    all_cafes = Cafe.query.all()
    result = {"cafe": []}
    for cafe in all_cafes:
        cafe.__dict__.pop("_sa_instance_state", None)
        result["cafe"].append(cafe.__dict__)
    return jsonify(result)


@app.route("/search", methods=["GET"])
def search():
    loc = request.args["loc"]  # get parameter from url
    cafes = Cafe.query.filter_by(location=loc).all()
    if len(cafes) > 0:
        result = {"cafe": []}
        for cafe in cafes:
            cafe.__dict__.pop("_sa_instance_state", None)
            result["cafe"].append(cafe.__dict__)
        return jsonify(result)
    else:
        message = {"error": {
            "Not found": "Sorry, we don't have a cafe at that location."}}
        return jsonify(message)


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():

    parameters = request.get_json()
    new_cafe = Cafe()
    new_cafe.name = parameters["name"]
    new_cafe.map_url = parameters["map_url"]
    new_cafe.img_url = parameters["img_url"]
    new_cafe.location = parameters["location"]
    new_cafe.has_sockets = parameters["has_sockets"]
    new_cafe.has_toilet = parameters["has_toilet"]
    new_cafe.has_wifi = parameters["has_wifi"]
    new_cafe.can_take_calls = parameters["can_take_calls"]
    new_cafe.seats = parameters["seats"]
    new_cafe.coffee_price = parameters["coffee_price"]
    db.session.add(new_cafe)
    db.session.commit()
    message = {"response": {"success": "Successfully added the new cafe."}}
    return jsonify(message)

# HTTP PUT/PATCH - Update Record


@app.route('/update-price/<int:id>', methods=["PATCH"])
def update_price(id):
    try:
        new_price = request.args["new-price"]
        cafe_to_update = Cafe.query.get(id)
    except KeyError:
        return jsonify({"error": "Invalid request"})
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        message = {"success": "Successfully updated the price."}
        return jsonify(message)
    else:
        message = {
            "error": {
                "Not found": "Sorry, a cafe with that id was not found in the database."}}
        return jsonify(message)

# HTTP DELETE - Delete Record


@app.route('/report-closed/<int:id>', methods=["DELETE"])
def report_closed(id):
    api_key = "q%QN3yRA5!XEGX*S"
    try:
        key = request.args["api-key"]
    except KeyError:
        return jsonify({"error": "Invalid request"})
    if key == api_key:
        closed_cafe = Cafe.query.get(id)
        if closed_cafe:
            db.session.delete(closed_cafe)
            db.session.commit()
            message = {"success": "Thanks for you feedback."}
            return jsonify(message)
        else:
            message = {
                "error": {
                    "Not found": "Sorry, a cafe with that id was not found in the database."}}
            return jsonify(message)
    else:
        message = {
            "error": "Sorry, that's not allowed.Make sure you have the correct key."}
        return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
