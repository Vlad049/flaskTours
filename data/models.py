from typing import List

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


Base = declarative_base()
db = SQLAlchemy(model_class=Base, engine_options=dict(echo=True))


user_tour_assoc = Table(
    "user_tour_assoc",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("tour_id", ForeignKey("tours.id"), primary_key=True)
)


class Tour(db.Model):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String())
    departure: Mapped[str] = mapped_column(String(100))
    picture: Mapped[str] = mapped_column(String())
    price: Mapped[int] = mapped_column()
    stars: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(300))
    nights: Mapped[int] = mapped_column()
    date: Mapped[str] = mapped_column(String(100))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    _password: Mapped[str] = mapped_column(String())
    tours: Mapped[List[Tour]] = relationship(secondary=user_tour_assoc)

    @property
    def password(self):
        return "Don`t use this"
    
    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def is_validate_password(self, pwd):
        return check_password_hash(self._password, pwd)
