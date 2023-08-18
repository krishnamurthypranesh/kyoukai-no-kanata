"""update_gid_col_type

Revision ID: 0002
Revises: 00001
Create Date: 2023-08-18 16:24:44.586737

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by almebic
revision = '0002'
down_revision = '00001'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('requests_received', 'request',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               comment='request body with headers',
               existing_nullable=False)
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('requests_received', 'request',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               comment=None,
               existing_comment='request body with headers',
               existing_nullable=False)
    # ### end Alembic commands ###