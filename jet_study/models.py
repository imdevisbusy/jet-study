from sqlalchemy import Integer, String, \
    Column, ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
user_timetable = Table('user_timetable', Base.metadata,
    Column('user_id', Integer, ForeignKey("user.id")),
    Column('timetable_id', Integer, ForeignKey("timetable.id"))
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    number = Column(Integer, nullable=False)


class Timetable(Base):
    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    lesson_number = Column(Integer, ForeignKey("lesson.number"))
    user = relationship("User", secondary=user_timetable, backref="timetable")
    