"""empty message

Revision ID: 0cad1043775e
Revises: 7b5bdf050798
Create Date: 2024-04-28 16:21:33.039059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cad1043775e'
down_revision = '7b5bdf050798'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('available_dates', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.drop_column('available_dates')

    # ### end Alembic commands ###
