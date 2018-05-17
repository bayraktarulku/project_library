import requests
from faker import Faker

BASE_URL = 'http://0.0.0.0:5000'

USER_COUNT = 3
AUTHOR_COUNT = 10

TYPES = ['Realistic', 'Picaresque', 'Historical',
         'Gothic', 'Detective', 'Science Fiction']


FACTORY = Faker()


def generate_user():
    return {'username': FACTORY.name(),
            'password': FACTORY.password(),
            'email': FACTORY.email(),
            'is_admin': 1,
            'is_active': 1}


def create_user(user):
    r = requests.post(
        BASE_URL + '/api/user',
        json={'username': user['username'],
              'password': user['password'],
              'email': user['email'],
              'is_admin': user['is_admin'],
              'is_active': user['is_active']})
    return r.json()


def get_users():
    r = requests.get(BASE_URL + '/api/user')
    # pprint("{} \n".format(r.json()))
    return r.json()


def generate_author():
    return {'fullname': FACTORY.name()}


def create_author(author):
    r = requests.post(
        BASE_URL + '/api/author',
        json={'fullname': author['fullname']})
    return r.json()


def get_authors():
    r = requests.get(BASE_URL + '/api/author')
    # pprint("{} \n".format(r.json()))
    return r.json()


def create_book(author_id, type_id):
    r = requests.post(
        BASE_URL + '/api/book',
        json={'name': FACTORY.first_name(),
              'type_id': type_id,
              'author_id': author_id,
              'book_translator': FACTORY.name()})
    return r.json()


def get_books():
    r = requests.get(BASE_URL + '/api/book')
    # pprint("{} \n".format(r.json()))
    return r.json()


def create_type(name):
    r = requests.post(BASE_URL + '/api/type', json={'name': name})
    return r.json()


def get_types():
    r = requests.get(BASE_URL + '/api/type')
    # pprint("{} \n".format(r.json()))
    return r.json()


if __name__ == '__main__':
    print('CREATE USERS')
    users = [generate_user() for _ in range(USER_COUNT)]
    for u in users:
        create_user(u)
    users = get_users()

    print('CREATE TYPES')
    for t in TYPES:
        create_type(t)
    types = get_types()

    print('CREATE AUTHOR')
    authors = [generate_author() for _ in range(AUTHOR_COUNT)]
    for a in authors:
        create_author(a)
    authors = get_authors()

    print('CREATE BOOKS')
    for a in authors['records']:
        for t in types['records']:
            create_book(a['id'], t['id'])
