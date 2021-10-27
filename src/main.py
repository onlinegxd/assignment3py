import json

from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import make_response
import jwt
from datetime import datetime, timedelta
from flask.json import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123321@localhost/Assignment3'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)
    token = db.Column('token', db.Unicode)

    def __init__(self, id, login, password, token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

    def __repr__(self):
        return '<"id": %r,"login": "%r","password": "%r","token": "%r">' % (self.id, self.login, self.password, self.token)


@app.route('/login')
def login():

    auth = request.authorization

    # givenpassword = request.form.get("password")
    # givenlogin = request.form.get("login")

    row = Users.query.filter_by(login=request.authorization["username"], password=request.authorization["password"]).first()

    if row is not None:
        token = jwt.encode({'user': auth.username, 'pass': auth.password, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        if row.token != token or row.token == 'Null':
            row.token = token
            db.session.commit()
        return f"Hello, {auth.username}, successfully logged in"
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected')
def protected():
    row = Users.query.filter_by(login=request.authorization["username"],
                                password=request.authorization["password"]).first()
    decoded_token = json.loads(json.dumps(jwt.decode(row.token, "secretkey", algorithms=["HS256"])))
    if row.login == decoded_token['user'] and row.password == decoded_token['pass']:
        return f"Hello, {decoded_token['user']}, token which is provided is correct"


if __name__ == '__main__':
    app.run(debug=True)
