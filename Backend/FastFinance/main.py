<<<<<<< Updated upstream
from fastapi import FastAPI, HTTPException
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
        role=Role.accountant,
        status=True,
        first_name="John",
        last_name="Accounting"
    )
]
=======
from calendar import month
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date, timedelta

import DummyDB
from userinfo import User, Role, NewUserRequest
from fastapi.middleware.cors import CORSMiddleware
from DummyDB import user_table, new_user_table

app = FastAPI()

uri = "mongodb+srv://FastFinancesAdmin:fastfin13@fastfinances.p3wik.mongodb.net/?retryWrites=true&w=majority&appName=FastFinances"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# adding a comment here
>>>>>>> Stashed changes

class Request(BaseModel):
    type: str = None
    req: str = None

@app.get("/")
async def root():
<<<<<<< Updated upstream
    return {"Greeting": "Hello team. I have successfully hosted my API through ngrok. I am on a roll tonight."}
=======
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        return e

    #return {"Greeting": "You have accessed the root of the FastFinance API."}
>>>>>>> Stashed changes

@app.get("/users")
async def fetch_users():
    return db

<<<<<<< Updated upstream
=======
@app.get("users/new_user")
async def get_new_user_requests():
    """
    Returns the list of new user requests.
    :return:
    """
    return new_user_table


@app.get("/users/login")
async def login(login_info: User):
    """
    This takes a special type of user with only 2 variables. the JSON format looks like:
    {"id": "user id string", "hashed_password": "hashed password string"}

    it will return a JSON with one field: "message", which includes the role of the user and " Login Successful", eg:
    {"message": "Accountant Login Successful"}
    {"message": "Manager Login Successful"}
    {"message": "Admin Login Successful"}

    depending on the user's role.

    :param login_info:
    :return:
    """

    DummyDB.check_outdated_passwords()
    # the above line is to check every current password in the system if they are about to expire, and send an email if so.
    # this happens during every login request because at least one user logging in is a very frequent and consistent action
    #

    user = DummyDB.get_user(login_info.id) #raises an exception if user id not found

    if user.hashed_pass == login_info.hashed_pass:
        if not user.status:
            raise HTTPException(401, detail={"Error": "Account Suspended"})
        if user.role == Role.admin:
            return {"message": "Admin Login Successful"}
        elif user.role == Role.manager:
            return {"message": "Accountant Login Successful"}
        else:
            return {"message": "Accountant Login Successful"}
    else:
        raise HTTPException(401, detail={"Error": "Unauthorized"})

@app.get("/users/login/forgot_password")
async def forgot_pass(login_info: User, answer_list):
    """
    This also takes a special user JSON, this time with just their ID and their email in the following format:
    {"id": <user id string>, "email": <email string>}

    if successful, it will return the user's security questions in the following json:
    {
        "security_question_1": <security question 1 string>,
        "security_question_2": <security question 2 string>,
        "security_question_3": <security question 3 string>,
        "security_answer_1": <security answer 1 string>,
        "security_answer_2": <security answer 2 string>,
        "security_answer_3": <security answer 3 string>,
    }
    It is expected that the web client will handle the logic. Once the answers have been verified, the client use the update_users()
    function defined by the path: /users/update with the "put" parameter
    :param answer_list:
    :param login_info:
    :return:
    """
    user = DummyDB.get_user(login_info.id)
    
    return {"security_question": user.security_question, "security_answer": user.security_answer}


# The primary way the admin will add a user to the system.
>>>>>>> Stashed changes
@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
#weird shit going on tonight

<<<<<<< Updated upstream
=======
@app.post("users/new_user")
async def new_user(user_req: NewUserRequest):
    """
    Function to create a "new user" request in the system.
    The format for a new user request JSON looks like:
    {
        "first_name": <first name string>
        "last_name": <last name string>
        "email": <email address string>
        "dob": <string in format dd/mm/yyyy>
    }
    Admins will see new user requests on their client.
    To create a new user in the database, use the post:"/users" api call.

    :param user_req:
    :return:
    """
    new_user_table.append(user_req)
    return {"email" : user_req.email}

# the primary way an admin will update user info.
# this includes changing personal info about the user and activating or deactivating them
>>>>>>> Stashed changes
@app.put("/users/update")
async def update_user(user: User):
    for u in db:
        if user.id == u.id:
            if user.hashed_pass is not None:
                u.hashed_pass = user.hashed_pass
            if user.email is not None:
                u.email = user.email
            if user.status is not None:
                u.status = user.status
            if user.first_name is not None:
                u.first_name = user.first_name
            if user.last_name is not None:
                u.last_name = user.last_name
            return {f"User with ID {user.id} updated successfully."}
    raise HTTPException(
        status_code=404,
        detail=f"User with ID: {user.id} does not exist."
<<<<<<< Updated upstream
    )
=======
    )

# @app.delete("/users/new_user")
# async def delete_new_user_request(email: str):
#     pass
>>>>>>> Stashed changes
