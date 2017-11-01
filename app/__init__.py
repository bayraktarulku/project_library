from flask import Flask, render_template
from app.api.user import api_bp as user_api_bp
from app.api.book_type import api_bp as type_api_bp
from app.api.author import api_bp as author_record_api


app = Flask(__name__)
app.register_blueprint(user_api_bp)
app.register_blueprint(type_api_bp)
app.register_blueprint(author_record_api)



@app.route('/')
def index():
    return render_template('index.html')
