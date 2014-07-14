from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dev.db', echo=False)
Base = declarative_base()
metadata = Base.metadata


def create_all():
    metadata.create_all(engine)
