from flask import render_template, request, redirect
from QLHS import app, dao, login
from flask_login import login_user, logout_user
from datetime import date


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/login")
def my_login():
    return render_template("login.html")


@app.route("/login", methods=['post'])
def login_process():
    username = request.form['username']
    password = request.form['password']
    u = dao.auth_user(username, password)
    if u:
        login_user(u)
        return redirect("/login")
    return render_template("/")


@app.route('/logout')
def my_logout():
    logout_user()
    return redirect("/")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/Tiepnhan')
def my_Tiepnhan():
    return render_template("Tiepnhan.html")




@app.route('/Danhsachlop')
def my_Danhsachlop():
    return render_template("Danhsachlop.html")


@app.route('/Bangdiem')
def my_Bangdiem():
    return render_template("Bangdiem.html")


@app.route('/Baocao')
def my_Baocao():
    return render_template("Baocao.html")


if __name__ == "__main__":
    app.run(debug=True)
