#Third party lib
from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

#Local files
from security import authenticate, identity
from resources.item_resource import Item, Items

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # this will create an end point /auth


api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')

if __name__ == "__main__":
    app.run(port=2000, debug=True)
