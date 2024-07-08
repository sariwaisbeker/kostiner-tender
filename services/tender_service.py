import json
from bson import ObjectId
import pandas as pd

from dal.tender_repo import tender_repo, DataAlreadyExistsError
from services.base_service import base_service


class tender_service(base_service):
    def __init__(self):
        self.repo = tender_repo()
        super().__init__(self.repo)
        print('in __init__ in tender_service')

    def insert_from_csv(self, file):
        result = []
        try:
            df = pd.read_csv(file)
            expected_columns = ['tender_id', 'category', 'tender_name', 'date', 'details__participants',
                                'details__disqualified_participants', 'details__committee_member']

            actual_columns = df.columns.tolist()

            if not all(col in actual_columns for col in expected_columns):
                raise ValueError(f"CSV file must contain columns: {', '.join(expected_columns)}")

            data = df.to_dict(orient='records')
            for row in data:
                try:
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
                except Exception as e:
                    print(f"Error processing row: {row}. Error: {e}")
                    continue
                result.append(tender)
            return self.repo.insert(result)
        except DataAlreadyExistsError as e:
            raise e
        except Exception as e:
            raise e
