from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from app.modules.authors import (create_author, get_authors,
                              get_author, delete_outhor)
from app.data_schemas import (AUTHOR_SCHEMA)
from schema import SchemaError


api_bp = Blueprint('author_record_api', __name__)
api = Api(api_bp)


class AuthorResource(Resource):

    def get(self):
        author_id = request.args.get('id', None)

        if author_id:
            record = get_author(author_id)
            print('record', record)

            return {'status': 'OK',
                    'record': record}

        record = get_authors()
        if not record:
            abort(401)

        return {'status': 'OK',
                'records': list(record)}

    def post(self):
        try:
            data = AUTHOR_SCHEMA.validate(request.json)
        except SchemaError:
            return {'status': 'error'}
        for key in data:
            if data[key] == '':
                return{'status': 'error'}

        author_type = create_author(data)
        return {'status': author_type['status'],
                'record': author_type}

    def delete(self):
        author_id = request.args.get('id', None)
        if not author_id:
            return {'status': 'error'}

        author = delete_outhor(author_id)

        return {'status': 'OK',
                'type': author}



api.add_resource(AuthorResource, '/api/author')