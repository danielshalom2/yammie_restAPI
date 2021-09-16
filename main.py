from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import Order


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
date_format = "%d-%m-%Y"
Order(api, db, date_format)

if __name__ == "__main__":
    app.run(debug=True)
