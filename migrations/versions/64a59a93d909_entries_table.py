"""entries table

Revision ID: 64a59a93d909
Revises: 
Create Date: 2023-07-19 17:51:45.643684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a59a93d909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('amount_due', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('student_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry')
    # ### end Alembic commands ###
