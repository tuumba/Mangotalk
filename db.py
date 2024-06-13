from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mangotok.db'
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create
