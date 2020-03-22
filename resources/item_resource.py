from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.item_model import ItemModel


items = []


class Item(Resource):
    # @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        print(item)
        if item:
            return item.json(), 200
        return {"message": "no item found"}, 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type=float,
                            required=True,
                            help="Something went wrong follow specification in the api docs")
        data = parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "item has been deleted"}
        return {"message": "No item with that name was found"}


class Items(Resource):
    def get(self):
        if len(items) > 0:
            return {"items": items}
        return {"message": "not item found"}, 404
