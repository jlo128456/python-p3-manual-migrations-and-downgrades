"""create table students

Revision ID: 122d7149c467
Revises: 791279dd0760
Create Date: 2025-04-16 22:02:56.612217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122d7149c467'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')