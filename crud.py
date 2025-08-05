from sqlalchemy.orm import Session
from models import User, Todo
from auth import get_password_hash
from schemas import UserCreate, TodoCreate

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: UserCreate) -> User:
    hashed_password = get_password_hash(user_data.password)
    db_user = User(email=user_data.email, hashed_password= hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_todo(db: Session, todo_data: TodoCreate, user_id: int) -> Todo:
    db_todo = Todo(**todo_data.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_user_todos(db: Session, user_id: int) -> list[Todo]:
    return db.query(Todo).filter(Todo.owner_id == user_id).all()

