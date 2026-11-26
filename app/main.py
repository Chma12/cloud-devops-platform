from fastapi import FastAPI

from app.database import Base, engine
from app.routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Task Manger API",
    description = "Cloud and DevOps personal project",
    version = "1.0.0",
)

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message":"Welcome to Task Manager API"}

@app.get("/health")
def health():
    return {"status":"healthy"}
