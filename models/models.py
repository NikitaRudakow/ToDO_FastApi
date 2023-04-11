from sqlalchemy import Table, MetaData, Integer, String, ForeignKey, Boolean, Column

metadata = MetaData()

task = Table(
    "task",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String, nullable=False),
    Column("done", Boolean),
    Column("subtask_id", Integer, ForeignKey("subtask.id"))
)

subtask = Table(
    "subtask",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String, nullable=False),
    Column("done", Boolean), 
    # Column("task_id", Integer, ForeignKey("task.id"))
)

