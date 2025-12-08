from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:1111@localhost:5432/qa"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
