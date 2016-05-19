"""empty message

Revision ID: c962813e4754
Revises: ca514d2fe5e5
Create Date: 2016-05-18 23:42:55.258737

"""

# revision identifiers, used by Alembic.
revision = 'c962813e4754'
down_revision = 'ca514d2fe5e5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('givelight_attendant',
    sa.Column('givelight_event_id', sa.String(length=1024), nullable=True),
    sa.Column('givelight_user_id', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['givelight_event_id'], ['givelight_event.id'], ),
    sa.ForeignKeyConstraint(['givelight_user_id'], ['givelight_user.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('givelight_attendant')
    ### end Alembic commands ###