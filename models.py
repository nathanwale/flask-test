from sqlalchemy import Column, Integer, Text, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class __Task:
    def __init__(self, id, description, done, completed_on, created) -> None:
        self.id = id
        self.description = description
        self.done = done
        self.completed_on = completed_on
        self.created = created

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text)
    done = Column(Boolean, default=False)
    completed_on = Column(DateTime)
    created = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Task<{self.id}>(description={self.description}, done={self.done}, completed_on={self.completed_on}, created={self.created})"
