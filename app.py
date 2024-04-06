import traceback

from flask import Flask, jsonify, request
import os
from routes import api_blueprint



app = Flask(__name__, static_url_path="/")
blueprints = (
    dict(blueprint=api_blueprint, url_prefix="/api", name="assessment_api"),
)
for blueprint in blueprints:
    app.register_blueprint(**blueprint)


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")


@app.route('/', methods=["GET"])
def index():
    return app.send_static_file("index.html")



if __name__ == "__main__":
    app.run(debug=True)
