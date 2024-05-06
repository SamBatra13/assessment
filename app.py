from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from routes import api_blueprint
from database import db
from flask_migrate import Migrate



app = Flask(__name__, static_url_path="/")
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///hospital_management.db'
db.init_app(app)
migrate = Migrate(app, db)
blueprints = (
    dict(blueprint=api_blueprint, url_prefix="/api", name="hospital_management_api"),
)
for blueprint in blueprints:
    app.register_blueprint(**blueprint)



if __name__ == "__main__":
    app.run(debug=True)
