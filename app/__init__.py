from flask import Flask, render_template
from flask_admin import Admin
from app.admin import (UserView, TypesView, AuthorsView, BooksView, NotesView)
from app.model import DBSession

from app.api.user import api_bp as user_api_bp
from app.api.book_type import api_bp as type_api_bp
from app.api.author import api_bp as author_record_api
from app.api.book import api_bp as book_record_api


app = Flask(__name__)
admin = Admin(app, name='Library', template_mode='bootstrap3', url='/')
admin.menu().pop()

app.register_blueprint(user_api_bp)
app.register_blueprint(type_api_bp)
app.register_blueprint(author_record_api)
app.register_blueprint(book_record_api)


admin.add_view(UserView)
admin.add_view(TypesView)
admin.add_view(AuthorsView)
admin.add_view(BooksView)
admin.add_view(NotesView)


@app.route('/')
def index():
    return 'OK'


@app.route('/home')
def home():
    return render_template('index.html')


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.teardown_request
def remove_session(ex=None):
    DBSession.expire_all()
