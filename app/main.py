from fastapi import FastAPI
from views.tasks import router as tasks_router


app = FastAPI(
    title="ToDO App"
)

app.include_router(tasks_router)
