from app.model import DBSession, Authors
from sqlalchemy import desc


def create_author(data):
    db_session = DBSession()
    new_author = Authors(**data)

    try:
        db_session.add(new_author)
        db_session.commit()

        result = {'status': 'OK',
                  'author': data['fullname']}
    except:
        db_session.rollback()
        result = {'status': 'error'}

    db_session.close()
    return result


def get_authors():
    db_session = DBSession()
    authors = db_session.query(Authors).order_by(desc(Authors.id)).all()

    for i in authors:
        yield {'id': i.id,
               'fullname': i.fullname}

    db_session.close()


def get_author(author_id):
    if not author_id:
        return {'status': 'Error'}
    else:
        db_session = DBSession()

        book_author = db_session.query(Authors).filter(
            Authors.id == author_id).all()

        if not book_author:
            return {'message': 'type not found'}

        book_author = [d.to_dict() for d in book_author]
        db_session.close()

        return {'author': book_author}


def delete_outhor(author_id):
    if not (author_id):
        return {'status': 'error'}
    print(type(author_id))
    db_session = DBSession()
    outhor = db_session.query(Authors).get(author_id)
    db_session.delete(outhor)
    db_session.commit()
    db_session.close()

    return {'status': 'OK'}
