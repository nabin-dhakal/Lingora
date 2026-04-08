from fastapi.routing import APIRouter

Router = APIRouter()

@Router.post("/register")
def Register():
    return {"message": "Register endpoint"}


@Router.get("/login")
def Login():
    return {"message": "Login endpoint"}