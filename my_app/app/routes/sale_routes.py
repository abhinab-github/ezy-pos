from flask import Blueprint, request, jsonify, send_file, url_for
from flask_jwt_extended import jwt_required
from app.models import Sale, Inventory, Customer
from app import db
from app.utils.pdf_generator import generate_sale_invoice
import os

bp = Blueprint('sale', __name__, url_prefix='/sale')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_sales():
    sales = Sale.query.all()
    sales_list = [sale.to_dict() for sale in sales]
    return jsonify(sales_list), 200

@bp.route('/', methods=['POST'])
@jwt_required()
def make_sale():
    data = request.get_json()

    # Fetch the customer and inventory item
    customer = Customer.query.get_or_404(data['customer_id'])
    inventory = Inventory.query.get_or_404(data['inventory_id'])

    # Calculate the selling price and apply any discount
    selling_price = data['selling_price']
    discount = data['discount_price']
    final_price = int(selling_price) - int(discount)

    # Create a new Sale entry with customer and item names
    sale = Sale(
        customer_id=customer.id,
        inventory_id=inventory.id,
        customer_name=customer.name,  # Store the customer name
        item_name=inventory.name,      # Store the item name
        discount_price=discount,
        payment_method=data['payment_method'],
        selling_price=selling_price,
        total_price=final_price,
        complete=True
    )

    # Update inventory status or quantity
    inventory.in_stock = False  # Mark as out of stock

    # Commit the sale and inventory status changes to the database
    db.session.add(sale)
    db.session.commit()

    # Generate the invoice PDF
    pdf_content = generate_sale_invoice(sale)

    # Define the path to save the PDF file
    invoice_dir = os.path.join('app', 'static', 'invoices')
    invoice_filename = f'invoice_{sale.id}.pdf'
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

@bp.route('/invoice/<int:sale_id>', methods=['GET'])
@jwt_required()
def download_invoice(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    
    # Path to where the invoice PDF is saved
    invoice_path = os.path.join('app', 'static', 'invoices', f'invoice_{sale.id}.pdf')
    
    # Print debug information
    print(f"Looking for invoice at: {invoice_path}")
    
    # Check if the invoice file exists
    if not os.path.exists(invoice_path):
        print(f"File not found: {invoice_path}")
        return jsonify({"message": "Invoice not found"}), 404
    
    # Serve the file as a downloadable attachment
    return send_file(invoice_path, mimetype='application/pdf', as_attachment=True, download_name=f'invoice_{sale.id}.pdf')
