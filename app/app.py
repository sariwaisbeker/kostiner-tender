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
api.add_namespace(namespace_user)
=======
app.before_request(before_request_middleware())
>>>>>>> a81d9a58b01b1a436f962582c9a5398d8fe11a05

if __name__ == '__main__':
    app.run(debug=True)
