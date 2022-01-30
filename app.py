from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:admin@localhost:3306/tutorial'
app.secret_key = "super secret key"
db= SQLAlchemy(app)

from controllers.datesController import *

if __name__ == '__main__':
    app.run(debug=True)