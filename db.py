from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# thing that going to link to the flask app, and look up the object and connect to database

@app.before_first_request
def create_tables():
	db.create_all()