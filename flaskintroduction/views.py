from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="chenster")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name') # i.e. /views/profile?name=chenster
    return render_template("index.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({'name': 'chenster', 'coolness': 100})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for('views.get_json'))