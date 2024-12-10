from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DBSettings():
    @staticmethod
    def get_session():
        engine = create_engine(f"postgresql+psycopg2://postgres:postgres@localhost:5432/database")
        return Session(binds=engine)