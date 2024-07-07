import csv
import json
from bson import ObjectId

class base_service:
    def __init__(self, repo):
        self.repo = repo
        print(f'in __init__ base_service implements {self.repo}')

    def get_all(self):
        print('in service in get method')
        return self.repo.get()

    def get_by_id(self, object_id):
        return self.repo.get_by_id(object_id)

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

    def update(self, object_id, data):
        return self.repo.update(object_id, data)

    def delete(self, object_id):
        return self.repo.delete(object_id)

