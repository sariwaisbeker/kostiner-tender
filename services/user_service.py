import json
from functools import wraps
from dal.user_repo import user_repo
from services.base_service import base_service


class user_service(base_service):
    def __init__(self):
        super().__init__(user_repo())
        self.repo = user_repo()
        print('in __init__ in user_service')

    def get_user_role(self):
        token_data = self.repo.decode_token()
        token_data_dict = {
            'message': token_data[0]['message']
        }
        print(token_data_dict)
        print(type(token_data_dict))
        if 'message' in token_data_dict:
            print('enter')
            return token_data_dict, 403
        return {'role': token_data['role']}

    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            result = self.get_user_role()
            if isinstance(result, dict) and 'role' in result:
                return f(result['role'], *args, **kwargs)
            return result

        return decorated
