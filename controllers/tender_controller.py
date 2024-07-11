from flask_restx import Resource, abort
from flask import request
from pymongo.results import InsertManyResult, InsertOneResult
from werkzeug.datastructures import FileStorage
import os

from dal.tender_repo import DataAlreadyExistsError
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


upload_parser = namespace.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True, help='CSV or Excel file')


@namespace.route('/post/upload')
class CSVUpload(Resource):
    @namespace.expect(upload_parser)
    def post(self):
        if 'file' not in request.files:
            abort(400, "No file part in the request")
        args = upload_parser.parse_args()
        file = args['file']
        print(f'tender controller args: {args}')
        print(f'tender controller file: {file}')

        if file.filename == '':
            abort(400, "No selected file")

        if not (file.filename.endswith('.csv') or file.filename.endswith('.xlsx') or file.filename.endswith('.xls')):
            abort(400, "File is not a CSV or Excel")

        try:
            if file.filename.endswith('.csv'):
                result = tender_service.insert_from_csv(file)

            elif file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
                result = tender_service.insert_from_excel(file)

            if isinstance(result, InsertManyResult):
                return 'The documents were successfully entered', 201

        except ValueError as e:
            abort(400, str(e))
        except DataAlreadyExistsError as e:
            abort(e.code, e.details)
        except Exception as e:
            abort(500, str(e))
        return {"message": "Unexpected error occurred"}, 500

@namespace.route('/post-tender')
class PostTender(Resource):
    @namespace.doc('post_tender')
    @namespace.expect(tender_model)
    @namespace.marshal_with(tender_model)
    def post(self):
        '''post tender by object'''
        new_tender = request.json
        print(f'tender controller post new_tender: {new_tender}')
        result = tender_service.create(new_tender)
        print(f'tender controller post result: {result}')
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
@namespace.response(204, 'No Content')
class DeleteTenderById(Resource):
    @namespace.doc('delete_tender')
    def delete(self, tender_id):
        '''delete tender by Id'''
        count_delete = tender_service.delete(tender_id)
        if count_delete is not None and count_delete > 0:
            return 'The tender deleted successfully'
        namespace.abort(404, f"tender {tender_id} doesn't exist")


namespace.add_resource(GetAllTenders, '/get-all-tenders')
namespace.add_resource(CSVUpload, '/post/upload')
namespace.add_resource(PostTender, '/post-tender')
namespace.add_resource(GetTenderById, '/get-id-tender/<string:tender_id>')
namespace.add_resource(PutTenderById, '/put-tender/<string:tender_id>')
namespace.add_resource(DeleteTenderById, '/delete-tender/<string:tender_id>')
