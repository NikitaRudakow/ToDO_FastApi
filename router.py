from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models.models import task, subtask
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import selectinload
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter(
    prefix="/tasks"
)

@router.get("/get_all_tasks")
async def get_all_tasks(session: AsyncSession = Depends(get_async_session)):
    query = select(task)
    result = await session.execute(query)
    tasks = result.fetchall()
    task_list = []
    for t in tasks:
        task_dict = {
            "id": t[0],
            "description": t[1],
            "done": t[2],
            "subtasks": []
        }
        subquery = select(subtask).where(subtask.c.task_id == t[0])
        subresult = await session.execute(subquery)
        subtasks = subresult.fetchall()
        for st in subtasks:
            subtask_dict = {
                "description": st[1],
                "done": st[2]
            }
            task_dict["subtasks"].append(subtask_dict)
        task_list.append(task_dict)
    return task_list




