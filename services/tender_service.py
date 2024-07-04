
from dal.tender_repo import tender_repo
from services.base_service import base_service

class tender_service(base_service):
    def __init__(self):
        super().__init__(tender_repo())
        self.repo = tender_repo()
        print('in __init__ in tender_service')

