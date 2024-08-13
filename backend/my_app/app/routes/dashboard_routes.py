from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.sql import func
from app.models import Purchase, Sale
from datetime import datetime
from app import db

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/daily', methods=['GET'])
@jwt_required()
def daily_data():
    today = datetime.utcnow().date()

    total_purchases = db.session.query(func.sum(Purchase.item_price * Purchase.units)).filter(func.date(Purchase.purchase_date) == today).scalar() or 0
    total_sales = db.session.query(func.sum(Sale.selling_price)).filter(func.date(Sale.sale_date) == today).scalar() or 0
    profit = total_sales - total_purchases

    return jsonify({
        "purchases": total_purchases,
        "sales": total_sales,
        "profit": profit
    }), 200

@bp.route('/monthly', methods=['GET'])
@jwt_required()
def monthly_data():
    current_month = datetime.utcnow().month
    current_year = datetime.utcnow().year

    total_purchases = db.session.query(func.sum(Purchase.item_price * Purchase.units)).filter(func.extract('month', Purchase.purchase_date) == current_month, func.extract('year', Purchase.purchase_date) == current_year).scalar() or 0
    total_sales = db.session.query(func.sum(Sale.selling_price)).filter(func.extract('month', Sale.sale_date) == current_month, func.extract('year', Sale.sale_date) == current_year).scalar() or 0
    profit = total_sales - total_purchases

    return jsonify({
        "purchases": total_purchases,
        "sales": total_sales,
        "profit": profit
    }), 200
