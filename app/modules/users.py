from app.model import DBSession, User
from datetime import datetime
# from pprint import pprint
from hashlib import sha512
from sqlalchemy import desc


def create_user(data):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    db_session = DBSession()
    print(data)
    user = db_session.query(User).filter(
        User.email == data['email']).first()
    if user:
        return {'status': 'error',
                'message': 'message'}
    password = sha512(data['password'].encode('utf-8')).hexdigest()
    new_user = User(
        username=data['username'], password=password,
        email=data['email'], confirmed_at=time, is_active=True,
        is_admin=data['is_admin'])

    try:
        db_session.add(new_user)
        db_session.commit()

        result = {'status': 'OK',
                  'user': data['username']}
    except:
        db_session.rollback()
        result = {'status': 'error'}

    db_session.close()
    return result


def update_user(user_id, data):
    data = {k: data[k] for k in data if k in ['username', 'password',
                                              'new_password', 'email']}
    db_session = DBSession()

    user = db_session.query(User).get(user_id)
    password = sha512(data['password'].encode('utf-8')).hexdigest()
    if (not user or user.password != password):
        return {'status': 'error'}
    if (user.password == password and data['new_password'] != ''):
        new_password = sha512(
            data['new_password'].encode('utf-8')).hexdigest()
        user.username = data['username']
        user.email = data['email']
        user.password = new_password
    elif (user.password == data['password'] and data['new_password'] == ''):
        user.username = data['username']
        user.email = data['email']
        user.password = data['password']
    else:
        return {'status': 'error'}
    db_session.commit()
    db_session.close()

    return {'status': 'OK',
            'user': user_id}


def get_users():
    db_session = DBSession()
    users = db_session.query(User).order_by(desc(User.id)).all()

    for i in users:
        yield {'id': i.id,
               'username': i.username,
               'email': i.email,
               'is_admin': i.is_admin,
               'confirmed_at': str(i.confirmed_at),
               'is_active': i.is_active}
    db_session.close()


def get_user(user_id):
    if not user_id:
        return {'status': 'Error'}
    else:
        db_session = DBSession()

        user = db_session.query(User).filter(User.id == user_id).all()
        if not user:
            return {'message': 'user not found'}

        user = [d.to_dict() for d in user]
        db_session.close()

        return {'user': user}


def delete_user(user_id, data):
    if not user_id:
        return{'status': 'error'}

    db_session = DBSession()
    user = db_session.query(User).get(user_id)
    password = sha512(data['password'].encode('utf-8')).hexdigest()
    if (not user or data['username'] != user.username or
            password != user.password):
        return{'status': 'error'}
    db_session.query(User).filter(User.id == user_id).delete()
    db_session.commit()
    db_session.close()

    return {'status': 'OK'}
