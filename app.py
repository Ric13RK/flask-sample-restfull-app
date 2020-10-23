from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
import os

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from security import authenticate, identity


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.envget(
    'FLASK_DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(
    os.getenv('FLASK_SQLALCHEMY_TRACK_MODIFICATIONS', 'False'))
app.config['PROPAGATE_EXCEPTIONS'] = bool(
    os.getenv('FLASK_PROPAGATE_EXCEPTIONS', 'True'))
# TODO: change ('Rishi') default app secret key to random 10 char key
app.secret_key = os.getenv('FLASK_APP_SECRET_KEY', 'Rishi')
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')

api.add_resource(ItemList, '/item/')
api.add_resource(StoreList, '/stores/')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    app.run(port=5000, debug=True)
