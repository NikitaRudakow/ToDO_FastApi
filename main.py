from fastapi import FastAPI

from router import router as tasks_router

app = FastAPI(
    title="ToDO App"
)

app.include_router(tasks_router)