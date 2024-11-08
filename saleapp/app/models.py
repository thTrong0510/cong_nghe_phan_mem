from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from saleapp.app import db, app


class category(db.Model):
    # __tablename__ = "category" tao ten cho bang khong thi bang se lay ten ham
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    products = relationship('Product', backref='category',
                            lazy=True)  # product de trong dau '' vi no chua biet product nao khi tao xong/co roi co tje de ngoai


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50))
    price = Column(Float, default=0)
    image = Column(String(200))
    category_id = Column(Integer, ForeignKey(category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all() # tao bang moi thi moi dung lenh nay create table
        # c1 = category(name='Mobile')
        # c2 = category(name='Tablet')
        # c3 = category(name='Laptop')
        c4 = category(name='printer')
        db.session.add(c4)
        db.session.commit()
        # db.session.add_all([c1, c2, c3]) #insert into
        # db.session.commit()

        products = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 3
        }, {
            "id": 4,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {
            "id": 5,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 2
        }, {
            "id": 6,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 3
        }, {
            "id": 7,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {
            "id": 8,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 2
        }]
        # for p in products:
        #     prod = Product(**p)
        #     db.session.add(prod)
        #
        # db.session.commit()
