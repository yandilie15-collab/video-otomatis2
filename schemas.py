from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str

class JobOut(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        orm_mode = True
