from model.user_model import UserModel

users = [
  UserModel(1,"Pedro","coco"),
  UserModel(2, "Marielys", "swde")
]

username_mapping = {user.username:user for user in users}
id_mapping = {user.id: user for user in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return id_mapping.get(user_id, None)
