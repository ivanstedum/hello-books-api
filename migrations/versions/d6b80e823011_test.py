"""test

Revision ID: d6b80e823011
Revises: 21392d6de333
Create Date: 2022-11-12 16:19:46.668966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6b80e823011'
down_revision = '21392d6de333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_genre',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )
    op.drop_table('book__genre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book__genre',
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], name='book__genre_book_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='book__genre_genre_id_fkey'),
    sa.PrimaryKeyConstraint('book_id', 'genre_id', name='book__genre_pkey')
    )
    op.drop_table('book_genre')
    # ### end Alembic commands ###
