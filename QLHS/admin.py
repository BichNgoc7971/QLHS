from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from QLHS import app, db, dao
from flask_login import logout_user, current_user
from flask import redirect


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__("ADMIN")


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(AuthenticatedView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html',
                           data=dao.revenue_by_product(),
                           cates=dao.count_product_by_cate())


class LogoutView(AuthenticatedView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin")


