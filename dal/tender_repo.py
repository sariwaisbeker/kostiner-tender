from dal.base_repo import base_repo

class tender_repo(base_repo):
    def __init__(self):
        super().__init__('Kostiner', 'tenders')
        print('in __init__ in trender_repo')

    def get_obj_id(self):
        return 'tender_id'
