# services/product_service.py
from ..models.product import db, Product

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(data):
    product = Product(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        stock=data.get('stock')
    )
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product_id, data):
    product = get_product_by_id(product_id)
    if not product:
        return None

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)

    db.session.commit()
    return product

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return False

    db.session.delete(product)
    db.session.commit()
    return True
