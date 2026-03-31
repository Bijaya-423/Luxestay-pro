from pydantic import BaseModel, Field
from datetime import date


class TaskCreate(BaseModel):
    room_id: int
    staff_id: int
    task_date: date
    notes: str | None = None



class TaskUpdate(BaseModel):
    room_id: int
    staff_id: int
    task_date: date
    status: str
    notes: str | None = None
    

# class TaskResponse(BaseModel):
#     id: int
#     room_id: int
#     staff_id: int
#     task_date: date
#     status: str
#     notes: str | None = None

#     class Config:
#         from_attributes = True


# class TaskListResponse(BaseModel):
#     tasks: list[TaskResponse]
#     total: int


# class TaskFilter(BaseModel):
#     room_id: int | None = None
#     staff_id: int | None = None
#     status: str | None = None
#     task_date: date | None = None


# class TaskStatsResponse(BaseModel):
#     total: int
#     pending: int
#     in_progress: int
#     completed: int


# class TaskHistoryResponse(BaseModel):
#     id: int
#     task_date: date
#     status: str
#     notes: str | None = None
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True

