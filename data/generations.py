import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from data.db_session import SqlAlchemyBase


class Generation(SqlAlchemyBase):
    __tablename__ = 'generations'

    num = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    generation_text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    comment = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=False)
