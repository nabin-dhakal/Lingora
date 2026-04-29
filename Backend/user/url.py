from fastapi.routing import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from auth.password import get_password_hash, verify_password
from auth.token import create_access_token
from .schema import UserCreate, UserLogin, Token
from .models import User

Router = APIRouter()

@Router.post("/register")
def Register(user: UserCreate, db : Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    

    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, username= user.username, full_name=user.full_name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.id}


@Router.post("/login")
def Login(user:UserLogin, db : Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == user.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(user.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(
        data= {"sub":user.email},
    )

    return {"access_token" : access_token, "token_type": "bearer"}
