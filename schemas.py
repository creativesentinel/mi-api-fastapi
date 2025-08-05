from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool = Field(default=True)

    class Config:
        from_attributes = True  # En Pydantic v2, orm_mode se cambió a from_attributes

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    priority: int = Field(default=1, ge=1, le=5)  # Prioridad entre 1 y 5

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    priority: int = 1

class TodoResponse(TodoBase):
    id: int
    owner_id: int
    complete: bool = Field(default=False)

    class Config:
        from_attributes = True