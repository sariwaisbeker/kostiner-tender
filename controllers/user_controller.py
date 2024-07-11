from flask_restx import Resource
from flask import request


from services import user_service
from models_swagger.user_model import nameSpace_user as namespace, user_model


@namespace.route('/get-all-users')
class GetAllUsers(Resource):
    @namespace.doc('list_user')
    @namespace.marshal_list_with(user_model)
    def get(self):
        '''get all users'''
        return user_service.get_all()

@namespace.route('/get-id-user/<string:user_id>')
@namespace.response(404, 'user not found')
class GetUserById(Resource):
    @namespace.doc('get_user')
    @namespace.marshal_with(user_model)
    def get(self, user_id):
        '''get user by Id'''
        user = user_service.get_by_id(user_id)
        if user:
            return user
        namespace.abort(404, f"user {user_id} doesn't exist")

@namespace.route('/post-user')
class PostUser(Resource):
    @namespace.doc('create_user')
    @namespace.expect(user_model)
    @namespace.marshal_with(user_model)
    def post(self):
        '''create a new user'''
        new_user = request.json
        result = user_service.create(new_user)
        print(result)
        return result, 201


@namespace.route('/put-user/<string:user_id>')
class PutUserById(Resource):
    @namespace.doc('update_user')
    @namespace.expect(user_model)
    @namespace.marshal_with(user_model)
    def put(self, user_id):
        '''update user by id'''
        update_user = request.json
        result = user_service.update(user_id, update_user)
        if result.modified_count > 0:
            updated_user = user_service.get_by_id(user_id)
            return updated_user
        namespace.abort(404, f"user {user_id} doesn't exist")


@namespace.route('/delete-user/<string:user_id>')
class DeleteUserById(Resource):
    @namespace.doc('delete_user')
    def delete(self, user_id):
        '''delete user by Id'''
        count_delete = user_service.delete(user_id)
        if count_delete is not None and count_delete > 0:
            return 'The user deleted successfully'
        namespace.abort(404, f"user {user_id} doesn't exist")

namespace.add_resource(GetAllUsers, '/get-all-users')
namespace.add_resource(PostUser, '/post-user')
namespace.add_resource(GetUserById, '/get-id-user/<string:user_id>')
namespace.add_resource(PutUserById, '/put-user/<string:user_id>')
namespace.add_resource(DeleteUserById, '/delete-user/<string:user_id>')