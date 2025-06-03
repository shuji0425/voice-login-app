from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: str
    password: str