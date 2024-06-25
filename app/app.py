from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from controllers.example_controller import nameSpace
from controllers.user_controller import namespace as namespace_user

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Kostiner Tender Records', description='Information from the world of auctions')

api.add_namespace(nameSpace)
<<<<<<< HEAD
<<<<<<< HEAD
api.add_namespace(namespace_user)
=======
app.before_request(before_request_middleware())
>>>>>>> a81d9a58b01b1a436f962582c9a5398d8fe11a05
=======
api.add_namespace(namespace_user, path='/users')
>>>>>>> 5fae81e (add user controller in all tier)

if __name__ == '__main__':
    print('in app')
    app.run(debug=True)
