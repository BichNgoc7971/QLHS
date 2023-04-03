from QLHS import db, app
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text, DateTime, Date
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_role = Column(String(20), default='USER')


class Student(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False)
    gioitinh = Column(String(10), nullable=False)
    ngaysinh = Column(Date, nullable=False)
    sdt = Column(String(20), nullable=False)
    diachi = Column(String(255), nullable=False)
    email = Column(String(255))


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # # import hashlib
        # u = User(name="ADMIN", username="admin", password=str(hashlib.md5("12345".encode('utf-8')).hexdigest()))
        # db.session.add(u)
        # db.session.commit()

        h = Student(hoten="Dang Luu Bich Ngoc", gioitinh='nu', sdt='0938807971',


        diachi = 'BinhDuong',
        email = '1954052064ngoc@ou.edu.vn')

        db.session.add(h)
        db.session.commit()
