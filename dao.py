from saleapp.app.models import category, Product

def load_categories():
    return category.query.order_by('id').all() #select * from

def load_products(cate_id=None, kw=None):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id: #check null, no value
        query = query.filter(Product.category_id == cate_id)

    return query.all()
