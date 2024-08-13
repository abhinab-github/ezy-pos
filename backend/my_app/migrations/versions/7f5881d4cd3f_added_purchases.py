"""added purchases

Revision ID: 7f5881d4cd3f
Revises: 
Create Date: 2024-08-13 20:47:30.575810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f5881d4cd3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('id_card_number', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('sku', sa.String(length=64), nullable=False),
    sa.Column('buy_price', sa.Float(), nullable=False),
    sa.Column('sale_price', sa.Float(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('in_stock', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=120), nullable=True),
    sa.Column('item_price', sa.Float(), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.Column('seller_name', sa.String(length=120), nullable=True),
    sa.Column('seller_address', sa.Text(), nullable=True),
    sa.Column('seller_id_card_number', sa.String(length=20), nullable=True),
    sa.Column('seller_email', sa.String(length=120), nullable=True),
    sa.Column('seller_phone', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('id_card_number', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('sale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('inventory_id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(length=120), nullable=True),
    sa.Column('item_name', sa.String(length=120), nullable=True),
    sa.Column('sale_date', sa.DateTime(), nullable=True),
    sa.Column('discount_price', sa.Float(), nullable=True),
    sa.Column('selling_price', sa.Float(), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('payment_method', sa.String(length=20), nullable=False),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['inventory_id'], ['inventory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    op.drop_table('user')
    op.drop_table('seller')
    op.drop_table('purchase')
    op.drop_table('inventory')
    op.drop_table('customer')
    # ### end Alembic commands ###
