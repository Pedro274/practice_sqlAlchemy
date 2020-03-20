from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="Something went wrong follow specification in the api doc")

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        if item:
            return {"item": item}, 200
        return {"message": "no item found"}, 404

    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None):
            return {"message": f"An item with the name of {name} already exist"}
        data = Item.parser.parse_args()
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)
        return new_item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {"message": "item has been deleted"}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda item: item["name"] == name, items), None)
        if item is None:
            item = {"name": name, "price": data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class Items(Resource):
    def get(self):
        if len(items) > 0:
            return {"items": items}
        return {"message": "not item found"}, 404