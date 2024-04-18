import json

from flask import Blueprint, render_template

with open("profiles.json", "r") as f:
    db = json.load(f)

profiles_blueprint = Blueprint(
    "profiles",
    __name__, 
    template_folder="template", 
    url_prefix="/profiles")

@profiles_blueprint.route("/") # /profiles
def index():
    return render_template("profiles/index.html", profiles=sorted(db, key=lambda x :x["last_name"]))

