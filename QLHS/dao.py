from QLHS.models import User, Student
from flask_login import current_user
from QLHS import db, app
from sqlalchemy import func
import hashlib


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()


def add_user(username, password, name):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password)
    db.session.add(u)
    db.session.commit()


def add_student(hoten, ngaysinh,
                sdt, diachi, email):
    h = Student(hoten=hoten, ngaysinh=ngaysinh,
                sdt=sdt, diachi=diachi,
                email=email)
    db.session.add(h)
    db.session.commit()


def get_hs_by_id(hs_id):
    return Student.query.get(hs_id)

