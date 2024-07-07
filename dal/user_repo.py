from flask import request
import jwt, os
from dotenv import load_dotenv
from dal.base_repo import base_repo

load_dotenv()


class user_repo(base_repo):
    def __init__(self):
        super().__init__('Kostiner', 'users')
        print('in __init__ in user_repo')

    def get_obj_id(self):
        return 'user_id'
    def decode_token(self):
        token = None
        if 'token' in request.cookies:
            token = request.cookies['token']
        if not token:
            return {'message': 'Token is missing!'}, 403
        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            return data
        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired!'}, 403
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token!'}, 403