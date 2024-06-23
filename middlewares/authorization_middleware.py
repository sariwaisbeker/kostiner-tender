from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request

def before_request_middleware():
    def middleware():
        if request.endpoint not in ('login', 'static'):
            try:
                verify_jwt_in_request()
            except Exception as e:
                return jsonify({"msg": "Unauthorized"}), 401
    return middleware