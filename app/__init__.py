from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mangotok.db'
db = SQLAlchemy(app)

@app.before_app_context
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
