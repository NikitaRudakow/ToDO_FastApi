from sqlalchemy import Table, MetaData, Integer, String, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship
from database import Base


class SubTask(Base):
    __tablename__ = "subtask"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    done = Column(Boolean)
    task_id = Column(Integer, ForeignKey('task.id', ondelete="CASCADE"))


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    done = Column(Boolean)
    subtasks = relationship(SubTask, uselist=True, cascade="save-update, merge, delete, delete-orphan")
