import csv
import json
from bson import ObjectId
from dal.tender_repo import tender_repo
from services.base_service import base_service

class tender_service(base_service):
    def __init__(self):
        self.repo = tender_repo()
        super().__init__(self.repo)
        print('in __init__ in tender_service')

    def create(self, path):
        result = []
        try:
            with open(path['csv_file_path'], 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tender = {
                        "tender_id": ObjectId(row['tender_id']),
                        "category": row['category'],
                        "tender_name": row['tender_name'],
                        "date": row['date'],
                        "details": {
                            "participants": json.loads(row['details__participants']),
                            "disqualified_participants": json.loads(row['details__disqualified_participants']),
                            "committee_member": row['details__committee_member']
                        }
                    }
                    result.append(tender)
            return self.repo.insert(result)
        except Exception as e:
            return e