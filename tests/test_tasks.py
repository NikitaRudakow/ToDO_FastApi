import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add_task(ac: AsyncClient):
    response = await ac.post("/tasks", json={
        "description": "Сходить в магазин",
        "done": False,
        "subtasks": [
            {
                "description": "купить хлеб",
                "done": False
            }
        ]
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_tasks(ac: AsyncClient):
    response = await ac.get("/tasks", params={
        "page": 1,
        "page_size": 10,
        "done": True
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_task_by_id(ac: AsyncClient):
    response = await ac.get("/tasks/1", params={
        "task_id": 1
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_task(ac: AsyncClient):
    response = await ac.put("/tasks/1", params={"task_id": 1}, json={
            "description": "Сходить в магазин",
            "done": True,
            "subtasks": [
                {
                    "id": 1,
                    "description": "купить кефир",
                    "done": True
                }
            ]
        }
    )
    asserted_response = {
        'id': 1, 
        'description': 'Сходить в магазин',
        'done': True,
        'subtasks': [
            {
                'id': 1, 
                'description': "купить кефир", 
                'done': True
            }
        ]
    }
    print(response.json())
    assert response.json() == asserted_response


@pytest.mark.asyncio
async def test_delete_task(ac: AsyncClient):
    response = await ac.delete("/tasks/1", params={
        "task_id": 1
    })
    assert response.json() == {"message": "Task deleted"}
