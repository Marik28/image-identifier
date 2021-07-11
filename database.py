from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings

DATABASE_URL = settings.database_url

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(bind=engine)

session = Session()


def get_session():
    try:
        yield session
    finally:
        session.close()
