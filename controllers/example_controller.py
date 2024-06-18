from flask_restx import Resource, fields
from services.example_service import dataService
from models.example_model import nameSpace, data_model

data_service = dataService()

@nameSpace.route('/')
class dataList(Resource):
    @nameSpace.doc('list_data')
    @nameSpace.marshal_list_with(data_model)
    def get(self):
        '''here write description of method'''
        return data_service.get_all_datas()

    # Other controllers methods
