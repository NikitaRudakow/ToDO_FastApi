from fastapi import APIRouter
from repositories.tasks import get_all_tasks as repo_get_all_tasks
from repositories.tasks import get_one_task as repo_get_one_task
from repositories.tasks import create_task as repo_create_task
from repositories.tasks import delete_task as repo_delete_task
from repositories.tasks import update_task as repo_update_task
from schemas.tasks import TaskSchema, ResponseShema, CreateTaskSchema, DeleteTaskSchema,TaskUpdateSchema


router = APIRouter(
)

@router.get("/tasks", response_model=ResponseShema)
async def get_all_tasks(page: int, page_size: int):
    result = await repo_get_all_tasks(page, page_size)
    return {"response": result}


@router.get("/tasks/{task_id}", response_model=ResponseShema)
async def get_one_task(task_id: int):
    result = await repo_get_one_task(task_id)
    return {"response": result}


@router.post("/tasks", response_model=TaskSchema)
async def create_task(task: CreateTaskSchema):
    result = await repo_create_task(task)
    return result


@router.delete("/tasks/{task_id}", response_model=DeleteTaskSchema)
async def delete_task(task_id: int):
    result = await repo_delete_task(task_id)
    if result:
        return {"message": "Task deleted"}
    else:
        return {"message": "Task not deleted"}


@router.put("/tasks/{task_id}", response_model=ResponseShema)
async def update_task(task_id: int, task_data: TaskUpdateSchema):
    result = await repo_update_task(task_id, task_data)
    return {"response": result}
