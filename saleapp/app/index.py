from flask import render_template, request
import dao
from cong_nghe_phan_mem.saleapp.app import app
import hashlib

@app.route("/")
def index():
    cates = dao.load_categories()
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    pages = request.args.get('page', 1)
    prods = dao.load_products(cate_id=cate_id, kw=kw, page=pages)
    quantity_page = dao.count_products()
    return render_template('index.html', categories=cates, products=prods, quantity_page=quantity_page)

@app.route("/login", methods=['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        pswd = request.form.get('pswd')
        # if dao.auth_user(username = username, pswd = pswd):


    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)