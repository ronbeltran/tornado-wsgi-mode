from sqlalchemy import Table, Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

from app.models import Base


class User(Base):
    __tablename__ = 'user'
    id         = Column(Integer, primary_key=True)
    username   = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=True)
    last_name  = Column(String(30), nullable=True)
    email      = Column(String(75), nullable=True)
    password   = Column(String(128), nullable=False)
    subscribers = relationship('Subscriber', backref='user')

    def __repr__(self):
        return "<User('%s')>" % (self.username)
