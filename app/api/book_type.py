from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from app.modules.type import (create_type, get_type, get_types, delete_type)
from app.data_schemas import (BOOK_TYPE_SCHEMA)
from schema import SchemaError


api_bp = Blueprint('type_record_api', __name__)
api = Api(api_bp)


class TypeResource(Resource):

    def get(self):
        type_id = request.args.get('id', None)

        if type_id:
            record = get_type(type_id)
            print('record', record)

            return {'status': 'OK',
                    'record': record}

        record = get_types()
        if not record:
            abort(401)

        return {'status': 'OK',
                'records': list(record)}

    def post(self):
        try:
            data = BOOK_TYPE_SCHEMA.validate(request.json)
        except SchemaError:
            return {'status': 'error'}
        for key in data:
            if data[key] == '':
                return{'status': 'error'}

        book_type = create_type(data)
        return {'status': book_type['status'],
                'record': book_type}

    def delete(self):
        type_id = request.args.get('id', None)
        if not type_id:
            return {'status': 'error'}

        book_type = delete_type(type_id)

        return {'status': 'OK',
                'type': book_type}



api.add_resource(TypeResource, '/api/type')