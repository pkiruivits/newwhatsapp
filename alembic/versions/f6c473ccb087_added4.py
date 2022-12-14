"""Added4

Revision ID: f6c473ccb087
Revises: fb6ef6ae5c83
Create Date: 2022-08-28 15:14:04.866617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6c473ccb087'
down_revision = 'fb6ef6ae5c83'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_smsinbound_Request_id', table_name='smsinbound')
    op.create_index(op.f('ix_smsinbound_Request_id'), 'smsinbound', ['Request_id'], unique=False)
    op.create_unique_constraint(None, 'smsinbound', ['sms_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'smsinbound', type_='unique')
    op.drop_index(op.f('ix_smsinbound_Request_id'), table_name='smsinbound')
    op.create_index('ix_smsinbound_Request_id', 'smsinbound', ['Request_id'], unique=False)
    # ### end Alembic commands ###
