from sqlalchemy import  Column,  Integer, String, Float, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database import Base, engine
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


class User(Base):
    __tablename__ = "user_fast"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    username = Column(String(100))
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

    student = relationship('Student', back_populates='user')


class Student(Base):
    __tablename__ = "student_fast"

    id = Column(Integer, primary_key=True)
    roll = Column(Integer, unique=True)
    name = Column(String(100))
    marks = Column(Float)
    user_id = Column(Integer, ForeignKey("user_fast.id"))

    user = relationship("User", back_populates="student")


Base.metadata.create_all(bind=engine)