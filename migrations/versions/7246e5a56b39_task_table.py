"""task table

Revision ID: 7246e5a56b39
Revises: 
Create Date: 2023-10-16 22:22:25.302671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7246e5a56b39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('effort', sa.Integer(), nullable=True),
    sa.Column('duedate', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_task_effort'), ['effort'], unique=False)
        batch_op.create_index(batch_op.f('ix_task_priority'), ['priority'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task_priority'))
        batch_op.drop_index(batch_op.f('ix_task_effort'))

    op.drop_table('task')
    # ### end Alembic commands ###