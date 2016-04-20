"""empty message

Revision ID: 15dd88ab3898
Revises: None
Create Date: 2016-04-20 02:10:16.889753

"""

# revision identifiers, used by Alembic.
revision = '15dd88ab3898'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('migrate_version')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('migrate_version',
    sa.Column('repository_id', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('repository_path', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('repository_id', name=u'migrate_version_pkey')
    )
    op.drop_table('user')
    ### end Alembic commands ###
