from models import (
    Base, Session, Book, engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    