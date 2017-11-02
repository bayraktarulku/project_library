from app.model import DBSession, Books
from sqlalchemy import desc


def create_book(data):
    db_session = DBSession()

    # book_type = db_session.query(Books).filter(
    #     Books.name == data['name'], Books.author.name==data['author']).first()
    # if book_type:
    #     return {'status': 'error',
    #             'message': 'message'}

    new_book = Books(name=data['name'], type_id=data['type_id'],
                     author_id=data['author_id'],
                     book_translator=data['book_translator'])

    try:
         db_session.add(new_book)
         db_session.commit()

         result = {'status': 'OK',
                   'book': data['name']}
    except:
        db_session.rollback()
        result = {'status': 'error'}

    db_session.close()
    return result


def get_books():
    db_session = DBSession()
    books = db_session.query(Books).order_by(desc(Books.id)).all()

    for b in books:
        yield {'id': b.id,
               'name': b.name}

    db_session.close()


def get_book(book_id):
    if not book_id:
        return {'status': 'Error'}
    else:
        db_session = DBSession()

        book = db_session.query(Books).filter(Books.id==book_id).all()

        if not book:
            return {'message': 'book not found'}

        book = [d.to_dict() for d in book]
        db_session.close()

        return {'book': book}

def delete_book(book_id):
    if not (book_id):
        return {'status': 'error'}

    db_session = DBSession()
    book = db_session.query(Books).get(book_id)
    db_session.delete(book)
    db_session.commit()
    db_session.close()

    return {'status': 'OK'}
