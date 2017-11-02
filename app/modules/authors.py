from app.model import DBSession, Authors
from sqlalchemy import desc


def create_author(data):
    db_session = DBSession()
    # print(db_session.query(Authors).filter(
    #     and_(Authors.name==data['name'], Authors.surname==data['surname'])).first())
    # book_author = db_session.query(Authors).filter(
    #     and_(Authors.name==data['name'], Authors.surname==data['surname'])).first()
    # print('WWWWWWWWWWWWWWWWWWWWW')
    # if book_author:
    #     return {'status': 'error',
    #             'message': 'message'}

    new_author = Authors(name=data['name'], surname=data['surname'])

    try:
        db_session.add(new_author)
        db_session.commit()

        result = {'status': 'OK',
                  'author_name': data['name'],
                  'author_surname': data['surname']}
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
               'name': i.name,
               'surname': i.surname}

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
