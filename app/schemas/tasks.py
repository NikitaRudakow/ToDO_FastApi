from pydantic import BaseModel
from typing import List, Optional


class BaseModelWithIdDescrDone(BaseModel):
    id: int
    description: str
    done: bool


class SubTaskSchema(BaseModelWithIdDescrDone):
    class Config:
        orm_mode = True


class TaskSchema(BaseModelWithIdDescrDone):
    class Config:
        orm_mode = True

    subtasks: Optional[List[SubTaskSchema]]


class ResponseShema(BaseModel):
    response: List[TaskSchema]


class CreateSubTaskSchema(BaseModel):
    description: str
    done: bool


class CreateTaskSchema(BaseModel):
    description: str
    done: bool
    subtasks: Optional[List[CreateSubTaskSchema]]


class DeleteTaskSchema(BaseModel):
    message: str



class TaskUpdateSchema(BaseModel):
    description: str
    done: bool
    subtasks: Optional[List[SubTaskSchema]]
