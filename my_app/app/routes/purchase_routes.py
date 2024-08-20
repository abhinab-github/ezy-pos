from flask import Blueprint, request, jsonify, url_for
from flask_jwt_extended import jwt_required
from app.models import Purchase, Inventory
from app import db
from app.utils.pdf_generator import generate_purchase_invoice
from datetime import datetime
import os

bp = Blueprint('purchase', __name__, url_prefix='/purchase')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_purchases():
    purchases = Purchase.query.all()
    return jsonify([purchase.to_dict() for purchase in purchases]), 200

@bp.route('/', methods=['POST'])
@jwt_required()
def make_purchase():
    data = request.get_json()

    # Fetch the Inventory item using the name provided
    # inventory = Inventory.query.filter_by(name=data['inventory_name']).first_or_404()

    # Create a new Purchase instance
    purchase = Purchase(
        item_name=data['inventory_name'],
        item_price=data['price'],  # Assuming the price per unit is provided
        units=data['units'],
        purchase_date=datetime.utcnow(),  # Store the current date and time
        seller_name=data['seller']['name'],
        seller_address=data['seller'].get('address'),
        seller_id_card_number=data['seller']['id_card_number'],
        seller_email=data['seller']['email'],
        seller_phone=data['seller']['phone']
    )
    db.session.add(purchase)
    
    # Mark the inventory item as in stock
    # inventory.in_stock = True
    db.session.commit()

    # Generate the purchase invoice
    pdf_content = generate_purchase_invoice(purchase)

    # Define the path to save the PDF file
    invoice_dir = os.path.join('app', 'static', 'invoices')
    invoice_filename = f'invoice_{purchase.item_name}_{purchase.seller_name}.pdf'
    invoice_path = os.path.join(invoice_dir, invoice_filename)

    # Ensure the directory exists
    os.makedirs(invoice_dir, exist_ok=True)

    # Save the PDF file to the specified location
    with open(invoice_path, 'wb') as f:
        f.write(pdf_content)

    # Generate the download URL for the invoice
    invoice_url = url_for('static', filename=f'invoices/{invoice_filename}', _external=True)

    # Return a success response with the invoice URL
    return jsonify({"message": "Sale completed", "invoice_url": invoice_url}), 201

    # Return the response with the invoice URL
    return jsonify({"message": "Purchase completed", "invoice_url": f"/invoices/{invoice_pdf}"}), 201