from flask import Flask, render_template
from app.api.user import api_bp as user_api_bp


app = Flask(__name__)
app.register_blueprint(user_api_bp)



@app.route('/')
def index():
    return render_template('index.html')
