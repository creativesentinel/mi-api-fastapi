from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SesionLocal, engine
from models import Base
from schemas import UserCreate, UserResponse, TodoCreate, TodoResponse 
from crud import get_user_by_email, create_user, create_todo, get_user_todos
from auth import create_access_token, verify_password, oauth2_scheme

app = FastAPI()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return create_user(db, user)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas")
    return {"access_token": create_access_token({"sub": user.email}), "token_type": "bearer"}

@app.post("/todos", response_model=TodoResponse)
def add_todo(todo: TodoCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_id = 1
    return get_user_todos(db, user_id)
