from flask import flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import UserMain # type: ignore
import bcrypt
app = flask(__name__)
# hash a password

password = b"supersecret"
salt = bcrypt.gensalt()
