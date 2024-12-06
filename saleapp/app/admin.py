from saleapp.app.models import Category, Product, User
from saleapp.app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from saleapp.app.models import UserRole
from flask import redirect


admin = Admin(app=app, name="eCommerce Admin")#, template_mode="bootstrap4")

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(User.user_role)

class CategoryView(AdminView):
    column_list = ["name", "Product"]

class ProductView(AdminView):
    can_export = True
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    page_size = 5
    column_editable_list = ['name']

class authenticated_view(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(User.user_role)

class logout_view(authenticated_view):
    @expose("/")
    def __index__(self):
        logout_user()
        return redirect("/admin")

class statsView(authenticated_view):
    @expose("/")
    def __index__(self):
        return self.render("admin/stats.html")


admin.add_view((CategoryView(Category, db.session)))
admin.add_view((ProductView(Product, db.session)))
admin.add_view((AdminView(User, db.session)))
admin.add_view((logout_view(name="Log Out")))
admin.add_view((statsView(name="Thong Ke")))