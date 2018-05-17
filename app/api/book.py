from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from app.modules.books import (create_book, get_books, get_book, delete_book)
from app.data_schemas import (BOOK_SCHEMA)
# from schema import SchemaError


api_bp = Blueprint('book_record_api', __name__)
api = Api(api_bp)


class BookResource(Resource):

    def get(self):
        book_id = request.args.get('id', None)

        if book_id:
            record = get_book(book_id)
            print('record', record)

            return {'status': 'OK',
                    'record': record}

        record = get_books()
        if not record:
            abort(401)

        return {'status': 'OK',
                'records': list(record)}

    def post(self):
        data = BOOK_SCHEMA.validate(request.json)
        book = create_book(data)
        return {'status': book['status'],
                'record': book}

    def delete(self):
        book_id = int(request.args.get('id', None))
        if not book_id:
            return {'status': 'error'}

        book = delete_book(book_id)

        return {'status': 'OK',
                'type': book}


api.add_resource(BookResource, '/api/book')
