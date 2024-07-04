from flask_restx import Resource
from services.example_service import dataService
from models_swagger.example_model import namespace, data_model

data_service = dataService()

@namespace.route('/')
class dataList(Resource):
    @namespace.doc('list_data')
    @namespace.marshal_list_with(data_model)
    def get(self):
        '''here write description of method'''
        return data_service.get_all_datas()

    # Other controllers methods
