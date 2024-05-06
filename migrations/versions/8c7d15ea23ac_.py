"""empty message

Revision ID: 8c7d15ea23ac
Revises: 303e1269b9c4
Create Date: 2024-05-06 11:27:30.215884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c7d15ea23ac'
down_revision = '303e1269b9c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('department', schema=None) as batch_op:
        batch_op.create_unique_constraint('Unique dept name', ['name'])

    with op.batch_alter_table('doctor', schema=None) as batch_op:
        batch_op.create_unique_constraint('Unique doctor email', ['email'])

    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.create_unique_constraint('Unique patient email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('doctor', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('department', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###