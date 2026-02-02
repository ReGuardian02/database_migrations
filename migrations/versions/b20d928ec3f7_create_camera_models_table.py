"""create camera models table

Revision ID: b20d928ec3f7
Revises: fc8131970898
Create Date: 2026-01-29 11:44:38.615375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b20d928ec3f7'
down_revision: Union[str, Sequence[str], None] = 'fc8131970898'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "camera_models",
        sa.Column("id", sa.Integer, primary_key=True),

        sa.Column("manufacturer", sa.String(256), nullable=True),
        sa.Column("model", sa.String(512), nullable=False),

        sa.Column("resolutionX", sa.Integer, nullable=True),
        sa.Column("resolutionY", sa.Integer, nullable=True),

        sa.Column("maxVirtualZoom", sa.Integer, server_default="9999", nullable=True),
        sa.Column("maxRealZoom", sa.Integer, server_default="36", nullable=True),

        sa.Column("focusMax", sa.Float, server_default="119", nullable=True),
        sa.Column("focusMin", sa.Float, server_default="3.3", nullable=True),

        sa.Column("MinFieldAngle", sa.Float, nullable=True),
        sa.Column("MaxFieldAngle", sa.Float, nullable=True),

        sa.Column("MinVerticalAngle", sa.Float, server_default="90", nullable=False),
        sa.Column("MaxVerticalAngle", sa.Float, server_default="15", nullable=False),

        sa.Column("streamDecFactor", sa.SmallInteger, server_default="2", nullable=False),

        sa.Column(
            "sectorLength",
            sa.Integer,
            server_default="28650",
            nullable=False
        ),

        sa.Column("ptzCalculator", sa.Boolean, server_default="0", nullable=True),
        sa.Column("wiper", sa.Boolean, server_default="0", nullable=True),
        sa.Column("defog", sa.Boolean, server_default="0", nullable=True),
        sa.Column("stabilizer", sa.Boolean, server_default="0", nullable=True),

        sa.Column("ptz", sa.Boolean, server_default="1", nullable=True),
        sa.Column("type", sa.Integer, server_default="0", nullable=True),

        sa.Column("invertPan", sa.Boolean, server_default="0", nullable=True),
        sa.Column("invertTilt", sa.Boolean, server_default="0", nullable=False),

        sa.Column("thermal", sa.Boolean, server_default="0", nullable=True),
        sa.Column("snapshoter", sa.Boolean, server_default="0", nullable=False),
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("camera_models")
