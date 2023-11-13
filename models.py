from sqlalchemy import (create_engine, Column, 
                        String, Integer, Date)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///books.db', echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column("Title", String)
    author = Column("Author", String)
    published_date = Column("Published", Date)
    price = Column("Price", Integer)

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.published_date}, Price: {self.price}"
