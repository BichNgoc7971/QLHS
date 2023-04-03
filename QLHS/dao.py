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


def get_student_by_id(student_id):
    return Student.query.get(student_id)


def add_student(ho, ten, gioitinh, ngaysinh,
                sdt, diachi, email):
    h = Student(ho=ho, ten=ten, gioitinh=gioitinh, ngaysinh=ngaysinh,
                sdt=sdt, diachi=diachi,
                email=email)
    db.session.add(h)
    db.session.commit()
