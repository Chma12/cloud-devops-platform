from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None

class  TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None
    done: bool = False

class TaskOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str]
    done: bool

