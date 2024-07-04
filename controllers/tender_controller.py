from flask_restx import Resource
from flask import request

from services import tender_service
from models_swagger.tender_model import namespace_tender as namespace, tender_model


@namespace.route('/get-all-tenders')
class GetAllTenders(Resource):
    @namespace.doc('list_tender')
    @namespace.marshal_list_with(tender_model)
    def get(self):
        '''get all tenders'''
        return tender_service.get_all()

@namespace.route('/get-id-tender/<string:tender_id>')
@namespace.response(404, 'tender not found')
class GetTenderById(Resource):
    @namespace.doc('get_tender')
    @namespace.marshal_with(tender_model)
    def get(self, tender_id):
        '''get tender by Id'''
        tender = tender_service.get_by_id(tender_id)
        if tender:
            return tender
        namespace.abort(404, f"tender {tender_id} doesn't exist")

@namespace.route('/post-tender')
class PostTender(Resource):
    @namespace.doc('create_tender')
    @namespace.expect(tender_model)
    @namespace.marshal_with(tender_model)
    def post(self):
        '''create a new tender'''
        new_tender = request.json
        result = tender_service.create(new_tender)
        print(result)
        return result, 201


@namespace.route('/put-tender/<string:tender_id>')
class PutTenderById(Resource):
    @namespace.doc('update_tender')
    @namespace.expect(tender_model)
    @namespace.marshal_with(tender_model)
    def put(self, tender_id):
        '''update tender by id'''
        update_tender = request.json
        result = tender_service.update(tender_id, update_tender)
        if result.modified_count > 0:
            updated_tender = tender_service.get_by_id(tender_id)
            return updated_tender
        namespace.abort(404, f"tender {tender_id} doesn't exist")


@namespace.route('/delete-tender/<string:tender_id>')
class DeleteTenderById(Resource):
    @namespace.doc('delete_tender')
    def delete(self, tender_id):
        '''delete tender by Id'''
        count_delete = tender_service.delete(tender_id)
        if count_delete is not None and count_delete > 0:
            return 'The tender deleted successfully'
        namespace.abort(404, f"tender {tender_id} doesn't exist")


namespace.add_resource(GetAllTenders, '/get-all-tenders')
namespace.add_resource(PostTender, '/post-tender')
namespace.add_resource(GetTenderById, '/get-id-tender/<string:tender_id>')
namespace.add_resource(PutTenderById, '/put-tender/<string:tender_id>')
namespace.add_resource(DeleteTenderById, '/delete-tender/<string:tender_id>')
