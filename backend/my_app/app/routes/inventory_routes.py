from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Inventory
from app import db

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_inventory():
    items = Inventory.query.all()
    return jsonify([item.to_dict() for item in items])

@bp.route('/', methods=['POST'])
@jwt_required()
def add_inventory():
    data = request.get_json()
    item = Inventory(
        name=data['name'],
        description=data.get('description'),
        sku=data['sku'],
        buy_price=data['buy_price'],
        sale_price=data['sale_price'],
        image_url=data.get('image_url'),
        in_stock=data.get('in_stock', True)
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_inventory(id):
    item = Inventory.query.get_or_404(id)
    data = request.get_json()
    item.name = data['name']
    item.description = data.get('description')
    item.sku = data['sku']
    item.buy_price = data['buy_price']
    item.sale_price = data['sale_price']
    item.image_url = data.get('image_url')
    item.in_stock = data.get('in_stock', True)
    db.session.commit()
    return jsonify(item.to_dict()), 200

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_inventory(id):
    item = Inventory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"}), 200
