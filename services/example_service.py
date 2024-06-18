from dal.example_repo import dataDAL

class dataService:
    def __init__(self):
        self.dal = dataDAL()

    def get_all_datas(self):
        return self.dal.get_all_datas()

    def get_data_by_id(self, data_id):
        return self.dal.get_data_by_id(data_id)

    # Other service methods
