from fastapi import APIRouter
from repositories.tasks import get_tasks as repo_get_tasks
from repositories.tasks import get_task_by_id as repo_get_task_by_id
from repositories.tasks import create_task as repo_create_task
from repositories.tasks import delete_task as repo_delete_task
from repositories.tasks import update_task as repo_update_task
from repositories.tasks import check_task_existence as repo_check_task_existence
from schemas.tasks import TaskSchema, ResponseShema, CreateTaskSchema, DeleteTaskSchema,TaskUpdateSchema


router = APIRouter(
)

@router.get("/tasks", response_model=ResponseShema)
async def get_tasks(page: int, page_size: int, done: bool):
    result = await repo_get_tasks(page, page_size, done)
    return {"response": result}


@router.get("/tasks/{task_id}", response_model=TaskSchema)
async def get_task_by_id(task_id: int):
    result = await repo_get_task_by_id(task_id)
    return result


@router.post("/tasks", response_model=TaskSchema)
async def create_task(task: CreateTaskSchema):
    result = await repo_create_task(task)
    return result


@router.delete("/tasks/{task_id}", response_model=DeleteTaskSchema)
async def delete_task(task_id: int):
    if await repo_check_task_existence(task_id):
        await repo_delete_task(task_id)
        return {"message": "Task deleted"}
    else:
        return {"message": "Task not found"}

@router.put("/tasks/{task_id}", response_model=TaskSchema)
async def update_task(task_id: int, task_data: TaskUpdateSchema):
    result = await repo_update_task(task_id, task_data)
    return result
