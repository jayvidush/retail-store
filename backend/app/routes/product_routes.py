# routes/product_routes.py
from flask import Blueprint, request, jsonify
from ..services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)

product_bp = Blueprint('product_routes', __name__)

@product_bp.route('/products', methods=['GET'])
def fetch_products():
    products = get_all_products()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def fetch_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.to_dict())

@product_bp.route('/products', methods=['POST'])
def create_new_product():
    data = request.json
    product = create_product(data)
    return jsonify(product.to_dict()), 201

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_existing_product(product_id):
    data = request.json
    product = update_product(product_id, data)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.to_dict())

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_existing_product(product_id):
    success = delete_product(product_id)
    if not success:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({"message": "Product deleted"}), 200
