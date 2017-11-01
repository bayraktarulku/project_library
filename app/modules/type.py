from app.model import DBSession, Types
from sqlalchemy import desc


def create_type(data):
    db_session = DBSession()

    book_type = db_session.query(Types).filter(
        Types.name == data['name']).first()
    if book_type:
        return {'status': 'error',
                'message': 'message'}

    new_type = Types(name=data['name'])

    try:
         db_session.add(new_type)
         db_session.commit()

         result = {'status': 'OK',
                   'type': data['name']}
    except:
        db_session.rollback()
        result = {'status': 'error'}

    db_session.close()
    return result


def get_types():
    db_session = DBSession()
    types = db_session.query(Types).order_by(desc(Types.id)).all()

    for i in types:
        yield {'id': i.id,
               'name': i.name}

    db_session.close()


def get_type(type_id):
    if not type_id:
        return {'status': 'Error'}
    else:
        db_session = DBSession()

        book_type = db_session.query(Types).filter(Types.id==type_id).all()

        if not book_type:
            return {'message': 'type not found'}

        book_type = [d.to_dict() for d in book_type]
        db_session.close()

        return {'type': book_type}

def delete_type(type_id):
    if not (type_id):
        return {'status': 'error'}

    db_session = DBSession()
    db_session.query(Types).filter(Types.id==type_id).delete()
    db_session.commit()
    db_session.close()

    return {'status': 'OK'}
