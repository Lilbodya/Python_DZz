from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True)
    subject_id = Column(Integer)
    level = Column(String)
    education_form = Column(String)
