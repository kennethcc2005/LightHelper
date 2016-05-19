"""empty message

Revision ID: ca514d2fe5e5
Revises: 60db277fe45d
Create Date: 2016-05-18 23:39:19.110169

"""

# revision identifiers, used by Alembic.
revision = 'ca514d2fe5e5'
down_revision = '60db277fe45d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('givelight_department',
    sa.Column('id', sa.String(length=1024), nullable=False),
    sa.Column('name', sa.String(length=1024), nullable=False),
    sa.Column('functions', sa.Text(), nullable=True),
    sa.Column('user_id', sa.String(length=1024), nullable=False),
    sa.Column('event_id', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['givelight_event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['givelight_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('givelight_department')
    ### end Alembic commands ###