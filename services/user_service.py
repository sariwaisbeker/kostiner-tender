from functools import wraps
from dal.user_repo import user_repo
from services.base_service import base_service

class user_service(base_service):
    def __init__(self):
        repo = user_repo()
        print(f'in __init__ in user_service')
        super().__init__(repo)

    def get_user_role():
        token_data = decode_token()
        if 'message' in token_data:
            return token_data
        return {'role': token_data['role']}

    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            result = get_user_role()
            if isinstance(result, dict) and 'role' in result:
                return f(result['role'], *args, **kwargs)
            return result

        return decorated