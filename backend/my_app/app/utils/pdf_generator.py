from io import BytesIO
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen import canvas
from app.models import Customer, Seller, Inventory

def generate_sale_invoice(sale):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    elements = []

    styles = getSampleStyleSheet()

    # Title and store information
    title = Paragraph("<b>SALE INVOICE</b>", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    store_info = """
    <b>EZY BUY SALE</b><br/>
    Patia, Bhubaneswar<br/>
    GSTIN: 324923048230
    """
    elements.append(Paragraph(store_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Fetch customer details
    customer = Customer.query.get(sale.customer_id)

    # Customer information
    customer_info = f"""
    <b>Customer Name:</b> {customer.name}<br/>
    <b>Address:</b> {customer.address}<br/>
    <b>Phone:</b> {customer.phone}<br/>
    <b>ID:</b> {customer.id_card_number}
    """
    elements.append(Paragraph(customer_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Invoice details table
    data = [
        ["Description", "Qty", "Selling Price", "Discount", "Total Amount"],
        [sale.item_name, 1, f"{sale.selling_price}", f"-{sale.discount_price}", f"{sale.total_price}"],
    ]

    table = Table(data, colWidths=[3 * inch, 1 * inch, 1.5 * inch, 1.5 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Footer
    footer = Paragraph("<b>Thank you for purchasing from EZY BUY SALE</b>", styles['Normal'])
    elements.append(Spacer(1, 12))
    elements.append(footer)

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def generate_purchase_invoice(purchase):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    elements = []

    styles = getSampleStyleSheet()

    # Title and store information
    title = Paragraph("<b>PURCHASE INVOICE</b>", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    store_info = """
    <b>EZY BUY SALE</b><br/>
    Patia, Bhubaneswar<br/>
    GSTIN: 324923048230
    """
    elements.append(Paragraph(store_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Fetch customer details
    # customer = Customer.query.get(sale.customer_id)

    # Customer information
    customer_info = f"""
    <b>Seller Name:</b> {purchase.seller_name}<br/>
    <b>Address:</b> {purchase.seller_address}<br/>
    <b>Phone:</b> {purchase.seller_phone}<br/>
    <b>ID:</b> {purchase.seller_id_card_number}
    """
    elements.append(Paragraph(customer_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Invoice details table
    data = [
        ["Description", "Qty", "Purchase Price", "Total Amount"],
        [purchase.item_name, 1, f"{purchase.item_price}", f"{purchase.item_price}"],
    ]

    table = Table(data, colWidths=[3 * inch, 1 * inch, 1.5 * inch, 1.5 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Footer
    footer = Paragraph("<b>Thank you for selling to EZY BUY SALE</b>", styles['Normal'])
    elements.append(Spacer(1, 12))
    elements.append(footer)

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
