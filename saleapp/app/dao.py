from cong_nghe_phan_mem.saleapp.app.models import category, Product
import math
from cong_nghe_phan_mem.saleapp.app import app
import hashlib
from models import User

def load_categories():
    return category.query.order_by('id').all() #select * from

def load_products(cate_id=None, kw=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id: #check null, no value
        query = query.filter(Product.category_id == cate_id)


    PAGE_SIZE = app.config["PAGE_SIZE"]
    start = (int(page) - 1) * PAGE_SIZE
    end = start + PAGE_SIZE
    query = query.slice(start, end)

    return query.all()

def count_products():
    return math.ceil(Product.query.count() / app.config["PAGE_SIZE"])

def auth_user(username, pswd):
    pswd = str(hashlib.md5(pswd.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username), User.password.__eq__(pswd))