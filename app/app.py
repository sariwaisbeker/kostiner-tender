from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from controllers.example_controller import nameSpace

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Kostiner Tender Records', description='Information from the world of auctions')

api.add_namespace(nameSpace)
app.before_request(before_request_middleware())

if __name__ == '__main__':
    app.run(debug=True)
