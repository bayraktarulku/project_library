from schema import Schema, Use

USER_SCHEMA = Schema({
    'username': Use(str),
    'password': Use(str),
    'email': Use(str),
    'is_admin': int,
    'is_active': int,
})


UPDATE_USER_SCHEMA = Schema({
    'username': Use(str),
    'password': Use(str),
    'new_password': Use(str),
    'email': Use(str),
})

DELETE_USER_SCHEMA = Schema({
    'username': Use(str),
    'password': Use(str), })

BOOK_TYPE_SCHEMA = Schema({
    'name': Use(str),
})

TYPE_SCHEMA = Schema({
    'name': Use(str),
})


AUTHOR_SCHEMA = Schema({
    'name': Use(str),
    'surname': Use(str),
})