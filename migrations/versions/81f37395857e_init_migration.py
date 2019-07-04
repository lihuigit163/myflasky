"""init migration

Revision ID: 81f37395857e
Revises: 
Create Date: 2019-07-05 00:12:41.313550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81f37395857e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('comfirmed', sa.Boolean(), nullable=True))
    op.add_column('Users', sa.Column('comfirmtime', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'comfirmtime')
    op.drop_column('Users', 'comfirmed')
    # ### end Alembic commands ###
