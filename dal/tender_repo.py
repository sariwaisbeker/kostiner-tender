from bson import ObjectId

from dal.base_repo import base_repo

class tender_repo(base_repo):
    def __init__(self):
        super().__init__('Kostiner', 'tenders')
        print('in __init__ in trender_repo')

    def get_obj_id(self):
        return 'tender_id'

    def insert(self, data):
        print(f'in tender_repo\nin insert: len(data):{len(data)}')
        result = []
        try:
            for item in data:
                if not self.collection.find_one({'tender_id': ObjectId(item['tender_id'])}):
                    result.append(item)
            if not result:
                print(f'if not exist new object {result}')
                return 400, "all the tenders already exists."
            temp = self.collection.insert_many(result)
            return result
        except Exception as e:
            print(f'in tender repo except Exception as e {e}')
            return e
