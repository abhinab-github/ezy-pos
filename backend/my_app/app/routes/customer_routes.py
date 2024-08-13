from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Customer
from app import db

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers])

@bp.route('/', methods=['POST'])
@jwt_required()
def add_customer():
    data = request.get_json()
    customer = Customer(
        name=data['name'],
        address=data.get('address'),
        phone=data['phone'],
        email=data['email'],
        id_card_number=data['id_card_number']
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    data = request.get_json()
    customer.name = data['name']
    customer.address = data.get('address')
    customer.phone = data['phone']
    customer.email = data['email']
    customer.id_card_number = data['id_card_number']
    db.session.commit()
    return jsonify(customer.to_dict()), 200

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted"}), 200
