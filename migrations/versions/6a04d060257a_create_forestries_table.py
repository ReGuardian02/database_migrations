"""create forestries table

Revision ID: 6a04d060257a
Revises: b20d928ec3f7
Create Date: 2026-01-30 12:07:50.113578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision: str = '6a04d060257a'
down_revision: Union[str, Sequence[str], None] = 'b20d928ec3f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "catalogs_forestries",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("code", sa.String(255), nullable=False),
        sa.Column("code_lv", sa.String(255), nullable=True),
        sa.Column("code_oiv", sa.String(255), nullable=True),
        sa.Column("polygon", Geometry(geometry_type="MULTIPOLYGON"), nullable=True),
        sa.Column("land_category", sa.Integer, nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("catalogs_forestries")
