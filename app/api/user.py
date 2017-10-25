from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from app.modules.users import (create_user, get_user, get_users, update_user,
                               delete_user)
from app.data_schemas import (USER_SCHEMA, UPDATE_USER_SCHEMA,
                                      DELETE_USER_SCHEMA)
from schema import SchemaError


api_bp = Blueprint('login_record_api', __name__)
api = Api(api_bp)


class LoginResource(Resource):

    def get(self):
        user_id = request.args.get('id', None)
        print(user_id)
        if user_id:
            record = get_user(user_id)
            print('record', record)
            return {'status': 'OK',
                    'record': record}

        record = get_users()
        if not record:
            abort(401)
        return {'status': 'OK',
                'records': list(record)}

    def post(self):
        print('asdad')
        try:
            data = USER_SCHEMA.validate(request.json)
        except SchemaError:
            return {'status': 'error'}
        for key in data:
            if data[key] == '':
                return{'status': 'error'}
        print(data)
        user = create_user(data)
        return {'status': user['status'],
                'record': user}

    def put(self):
        user_id = request.args.get('id', None)
        if not user_id:
            return {'status': 'Error'}
        try:
            data = UPDATE_USER_SCHEMA.validate(request.json)
        except SchemaError:
            return {'status': 'error',
                    'message': 'Missing or incorrect parameters'}

        if data['password'] == '':
            return {'status': 'error'}
        data['new_password'] = data[
            'new_password'] if 'new_password' in data else ''

        user = update_user(user_id, data)

        return {'status': 'OK',
                'user': user}

    def delete(self):
        user_id = request.args.get('id', None)
        if not user_id:
            return{'status': 'error'}
        try:
            data = DELETE_USER_SCHEMA.validate(request.json)
        except Exception:
            return {'status': 'error',
                    'message': 'Missing or incorrect parameters'}
        user = delete_user(user_id, data)

        return {'status': 'OK',
                'user': user}

api.add_resource(LoginResource, '/api/user')