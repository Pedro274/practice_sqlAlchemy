#Third party lib
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#Local files
from security import authenticate, identity
from resources.item_resource import Item, Items
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'gre432jrt$ej'

api = Api(app)
jwt = JWT(app, authenticate, identity)  # this will create an end point /auth
db = db.init_app(app)



api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')

if __name__ == "__main__":
    app.run(port=2000, debug=True)
