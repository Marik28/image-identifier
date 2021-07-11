import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

from settings import settings

Base = declarative_base()


class Image(Base):
    __tablename__ = "images"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    filename = sa.Column(sa.String, nullable=False)
    liked = sa.Column(sa.Boolean)


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        sa.CheckConstraint(
            f"length(username) >= {settings.username_min_len} and length(username) < {settings.username_max_len}",
            "Username length constraint",
        )
    )
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True)
    username = sa.Column(sa.String, unique=True)
    password_hash = sa.Column(sa.String)
