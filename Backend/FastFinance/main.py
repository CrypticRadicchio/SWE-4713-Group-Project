from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from userinfo import User, Role, Status

app = FastAPI()

db: List[User] = [
    User(
        id="testAdmin",
        hashed_pass="temp",
        # email is default for now so this test user can receive emails
        role = Role.admin,
        status=True,
        first_name="Dave",
        last_name="Administrator"
    ),
    User(
        id="sampleAccountant",
        hashed_pass="temp",
        # email is default for now so this test user can receive emails
        role=Role.accountant,
        status=True,
        first_name="John",
        last_name="Accounting"
    )
]

class Request(BaseModel):
    type: str = None
    req: str = None

@app.get("/")
async def root():
    return {"Greeting": "Hello team. I have successfully hosted my API through ngrok. I am on a roll tonight."}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/postuser")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
#weird shit going on tonight
