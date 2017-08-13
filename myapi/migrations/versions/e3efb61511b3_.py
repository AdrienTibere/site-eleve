"""empty message

Revision ID: e3efb61511b3
Revises: 
Create Date: 2017-08-11 16:00:50.376604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3efb61511b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('objective_model')
    op.drop_table('chapter_model')
    op.drop_table('objective')
    op.add_column('chapter', sa.Column('available', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chapter', 'available')
    op.create_table('objective',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('chapter_id', sa.INTEGER(), nullable=True),
    sa.Column('nb', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=125), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], [u'chapter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chapter_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nb', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('class_id', sa.INTEGER(), nullable=True),
    sa.Column('color', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('objective_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('chapter_id', sa.INTEGER(), nullable=True),
    sa.Column('nb', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=125), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
