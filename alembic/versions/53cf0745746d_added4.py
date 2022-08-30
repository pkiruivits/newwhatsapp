"""Added4

Revision ID: 53cf0745746d
Revises: f6c473ccb087
Create Date: 2022-08-30 11:24:20.352164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53cf0745746d'
down_revision = 'f6c473ccb087'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('smsinbound', sa.Column('list_reply_id', sa.String(), nullable=True))
    op.add_column('smsinbound', sa.Column('reply_tittle', sa.String(), nullable=True))
    op.add_column('smsinbound', sa.Column('reply_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('smsinbound', 'reply_description')
    op.drop_column('smsinbound', 'reply_tittle')
    op.drop_column('smsinbound', 'list_reply_id')
    # ### end Alembic commands ###
