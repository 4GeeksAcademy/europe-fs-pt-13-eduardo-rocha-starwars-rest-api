"""empty message

Revision ID: 0706d598f5d6
Revises: 9803b2b8f61c
Create Date: 2023-10-06 19:25:06.624553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0706d598f5d6'
down_revision = '9803b2b8f61c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=350), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('url')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=350), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('url')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=350), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('url')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=350), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('url')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('favorites')
    op.drop_table('characters')
    # ### end Alembic commands ###
