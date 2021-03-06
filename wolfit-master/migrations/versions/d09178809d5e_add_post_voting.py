"""empty message

Revision ID: d09178809d5e
Revises: e4278061c9f1
Create Date: 2018-08-21 16:50:14.905431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d09178809d5e"
down_revision = "e4278061c9f1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_vote",
        sa.Column("user.id", sa.Integer(), nullable=False),
        sa.Column("post.id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post.id"], ["post.id"]),
        sa.ForeignKeyConstraint(["user.id"], ["user.id"]),
        sa.PrimaryKeyConstraint("user.id", "post.id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_vote")
    # ### end Alembic commands ###
