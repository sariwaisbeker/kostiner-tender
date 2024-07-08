import csv, os
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
        print(f'in tender_service\ntender_service in create')
        result = []
        try:
            file_name, file_extension = os.path.splitext(path)
            print(f"tender_service File extension: {file_extension}")
            if file_extension != '.csv':
                raise ValueError("Invalid file extension. Expected '.csv'.")
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
            print(f'tender_service the result {result}')
            return self.repo.insert(result)
        except ValueError as e:
            raise e
        except FileNotFoundError as e:
            print("The specified file does not exist.")
            raise e
        except IsADirectoryError as e:
            print("The specified path is a directory.")
            raise e
        except OSError as e:
            print(f"OS error occurred: {e}")
            raise e
        except Exception as e:
            print(f'tender_service in except\ntender_service the except: {str(e)}')
            raise e
