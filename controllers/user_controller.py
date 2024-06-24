from flask_restx import Resource

from services.user_service import userService
from models_swagger.user_model import nameSpace_user as namespace, user_model


@namespace.route('/')
class userList(Resource):
    def __init__(self, *args, **kwargs):
        super(userList, self).__init__(*args, **kwargs)
        self.user_service = userService()

    @namespace.doc('list_user')
    @namespace.marshal_list_with(user_model)
    def get(self):
        '''get all users'''
        return self.user_service.get()

    @namespace.doc('create_user')
    @namespace.expect(user_model)
    @namespace.marshal_with(user_model, code=201)
    def post(self, user):
        '''create a new user'''
        new_user = namespace.payload
        return self.user_service.insert(new_user), 201



@namespace.route('/<int:user_id>')
@namespace.response(404, 'user not found')
class user(Resource):
    def __init__(self, *args, **kwargs):
        super(user, self).__init__(*args, **kwargs)
        self.user_service = userService()

    @namespace.doc('get_user')
    @namespace.marshal_with(user_model)
    def get(self, user_id):
        '''get user by Id'''
        user = self.user_service.get_by_id(user_id)
        if user:
            return user
        namespace.abort(404, f"user {user_id} doesn't exist")