from flask_admin.contrib.sqla import ModelView
from app.model import (DBSession, User, Types, Authors, Books, Notes)
from wtforms.fields import PasswordField
# from wtforms import TextAreaField
ModelView.page_size = 1000
ModelView.create_modal = True
ModelView.edit_modal = True

admin_session = DBSession()


class UserViewTemplate(ModelView):
    column_list = ['id', 'username', 'email', 'password', 'is_active',
                   'is_admin']
    column_exclude_list = ['password']
    form_overrides = dict(password=PasswordField)
    column_searchable_list = ['username', 'email']


class TypesViewTemplate(ModelView):
    column_list = ['id', 'name']
    column_searchable_list = ['id', 'name']


class AuthorsViewTemplate(ModelView):
    column_list = ['id', 'fullname']
    column_searchable_list = ['id', 'fullname']


class BooksViewTemplate(ModelView):
    column_list = ['id', 'author.fullname', 'type.name', 'book_translator']
    column_labels = {'author.fullname': 'Author', 'type.name': 'Type'}
    column_searchable_list = ['id', 'type.name',
                              'author.fullname', 'book_translator']


class NotesViewTemplate(ModelView):
    column_list = ['id', 'title', 'book.name', 'text', 'user.username']
    column_labels = {'book.name': 'Book Name', 'user.username': 'User'}

    column_searchable_list = ['id', 'title',
                              'book.name', 'text', 'user.username']

UserView = UserViewTemplate(User, admin_session,
                            name='Users',
                            category='User Menu')
TypesView = TypesViewTemplate(Types, admin_session,
                              name='Types',
                              category='Type Menu')
AuthorsView = AuthorsViewTemplate(Authors, admin_session,
                                  name='Authors',
                                  category='Authors Menu')
BooksView = BooksViewTemplate(Books, admin_session,
                              name='Books',
                              category='Books Menu')
NotesView = NotesViewTemplate(Notes, admin_session,
                              name='Notes',
                              category='Notes Menu')
