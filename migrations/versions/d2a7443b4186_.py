"""empty message

Revision ID: d2a7443b4186
Revises: 
Create Date: 2020-05-17 06:56:14.358832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2a7443b4186'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'update_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('update_time', mysql.DATETIME(), nullable=False))
    # ### end Alembic commands ###
