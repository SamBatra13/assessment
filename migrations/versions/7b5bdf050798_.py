"""empty message

Revision ID: 7b5bdf050798
Revises: 144dea108244
Create Date: 2024-04-28 14:36:51.227680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5bdf050798'
down_revision = '144dea108244'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('doctor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_appointment_doctor', 'doctor', ['doctor_id'], ['id'])

    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.drop_column('available_dates')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('available_dates', sa.VARCHAR(length=200), nullable=True))

    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('doctor_id')

    # ### end Alembic commands ###