from typing import List
from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from database import async_session_maker
from models.tasks import Task, SubTask
from schemas.tasks import CreateTaskSchema, TaskUpdateSchema


async def get_all_tasks(page: int, page_size: int) -> List[Task]:
    session = async_session_maker()
    async with session.begin():
        query = select(Task).options(selectinload(Task.subtasks)).offset((page - 1) * page_size).limit(page_size)
        result = await session.scalars(query)
    return result.all()


async def get_one_task(task_id: int):
    session = async_session_maker()
    async with session.begin():
        query = select(Task) \
            .options(selectinload(Task.subtasks)) \
            .where(Task.id == task_id)
        result = await session.scalars(query)
    await session.close()
    return result.all()


async def create_task(task_data: CreateTaskSchema):
    session = async_session_maker()
    subtasks = []
    async with session.begin():
        task = Task(description=task_data.description, done=task_data.done)
        session.add(task)
        await session.flush()
        task_id = task.id
        for subtask_data in task_data.subtasks:
            subtask = SubTask(description=subtask_data.description, done=subtask_data.done, task_id=task_id)
            session.add(subtask)
            await session.flush()
            subtasks.append({"id": subtask.id, "description": subtask.description, "done": subtask.done})
        await session.commit()
    return {"id": task.id, "description": task.description, "done": task.done, "subtasks": subtasks}


async def delete_task(task_id: int):
    session = async_session_maker()
    async with session.begin():
        query = (delete(Task).where(Task.id == task_id))
        result = await session.execute(query)
    await session.close()
    return result.rowcount > 0


async def update_task(task_id: int, task_data: TaskUpdateSchema):
    session = async_session_maker()
    async with session.begin():
        query = update(Task).values(description=task_data.description, done=task_data.done).where(Task.id == task_id)
        await session.execute(query)

        for subtask_data in task_data.subtasks:
            subtask_id = subtask_data.id
            if subtask_id:
                query = update(SubTask).values(description=subtask_data.description, done=subtask_data.done).where(
                    SubTask.id == subtask_id)
                await session.execute(query)

        await session.commit()
    return await get_one_task(task_id)