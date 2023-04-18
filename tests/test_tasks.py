import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add_task(ac: AsyncClient):
    response = await ac.post("http://127.0.0.1:8000/tasks", json={
        "description": "Сходить в магазин",
        "done": False,
        "subtasks": [
            {
                "description": "купить молоко",
                "done": False
            },
            {
                "description": "купить хлеб",
                "done": False
            }
        ]
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_tasks(ac: AsyncClient):
    response = await ac.get("http://127.0.0.1:8000/tasks", params={
        "page": 1,
        "page_size": 10
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_one_tasks(ac: AsyncClient):
    response = await ac.get("http://127.0.0.1:8000/tasks/1", params={
        "task_id": 1
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_task(ac: AsyncClient):
    response = await ac.delete("http://127.0.0.1:8000/tasks/1", params={
        "task_id": 1
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_task(ac: AsyncClient):
    response = await ac.delete("http://127.0.0.1:8000/tasks/1", params={
        "task_id": 1
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_task(ac: AsyncClient):
    response = await ac.put(
        "http://127.0.0.1:8000/tasks/4", params={"task_id": 4},
        json={
            "description": "Сходить в магазин",
            "done": True,
            "subtasks": [
                {
                    "id": 7,
                    "description": "купить кефир",
                    "done": True
                }
            ]
        }
    )
    assert response.status_code == 200
