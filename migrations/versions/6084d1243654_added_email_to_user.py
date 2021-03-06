"""added email to user

Revision ID: 6084d1243654
Revises: 962e2f08000d
Create Date: 2019-04-09 12:18:05.847593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6084d1243654'
down_revision = '962e2f08000d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
