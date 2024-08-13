from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
            # Note: Password hash should generally not be exposed in a to_dict method
        }

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sku = db.Column(db.String(64), unique=False, nullable=False)
    buy_price = db.Column(db.Float, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)  # Default sale price
    image_url = db.Column(db.String(255), nullable=True)
    in_stock = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'sku': self.sku,
            'buy_price': self.buy_price,
            'sale_price': self.sale_price,
            'image_url': self.image_url,
            'in_stock': self.in_stock
        }

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.Text, nullable=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    id_card_number = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'id_card_number': self.id_card_number
        }

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    customer_name = db.Column(db.String(120), nullable=True)  # New field for storing customer name
    item_name = db.Column(db.String(120), nullable=True)      # New field for storing item name
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    discount_price = db.Column(db.Float, nullable=True, default=0.0)  # Field for discount price
    selling_price = db.Column(db.Float, nullable=True)  # Field for selling price
    total_price = db.Column(db.Float, nullable=True)    # Field for total price (selling_price - discount_price)
    payment_method = db.Column(db.String(20), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    customer = db.relationship('Customer', backref=db.backref('sales', lazy=True))
    inventory = db.relationship('Inventory', backref=db.backref('sales', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'item_name': self.item_name,
            'sale_date': self.sale_date,
            'discount_price': self.discount_price,
            'selling_price': self.selling_price,
            'total_price': self.total_price,
            'payment_method': self.payment_method,
            'complete': self.complete
        }

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.Text, nullable=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    id_card_number = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'id_card_number': self.id_card_number
        }

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Item details
    item_name = db.Column(db.String(120), nullable=True)  # Store the name of the item
    item_price = db.Column(db.Float, nullable=True)       # Store the price per unit
    units = db.Column(db.Integer, nullable=True)          # Store the number of units purchased
    
    # Purchase details
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)  # Store the date of purchase
    
    # Seller details
    seller_name = db.Column(db.String(120), nullable=True)          # Store the seller's name
    seller_address = db.Column(db.Text, nullable=True)               # Store the seller's address
    seller_id_card_number = db.Column(db.String(20), nullable=True) # Store the seller's ID card number
    seller_email = db.Column(db.String(120), nullable=True)         # Store the seller's email
    seller_phone = db.Column(db.String(20), nullable=True)          # Store the seller's phone number
    
    def to_dict(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'item_price': self.item_price,
            'units': self.units,
            'purchase_date': self.purchase_date,
            'seller_name': self.seller_name,
            'seller_address': self.seller_address,
            'seller_id_card_number': self.seller_id_card_number,
            'seller_email': self.seller_email,
            'seller_phone': self.seller_phone
        }
