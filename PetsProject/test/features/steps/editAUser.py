import dataclasses
from behave import when
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
from PetsProject.src.entity.user import User

@when("the user edit the information of a user")
def edit_a_user(context):
    username = Controller.getUserName()
    for row in context.table:
        context.username = str(row['username'])
        context.firstname = str(row['firstName'])
        context.lastname = str(row['lastName'])
        context.email = str(row['email'])
        context.password = str(row['password'])
        context.phone = str(row['phone'])
        context.userStatus = int(row['userStatus'])
    body_user = dataclasses.asdict(
        User(
            username=context.username,
            firstName=context.firstname,
            lastName=context.lastname,
            email=context.email,
            password=context.password,
            phone=context.phone,
            userStatus=context.userStatus
        )
    )
    head_user = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().put(endpoint=f"/user/{username}", headers=head_user, payload=body_user))
    Controller.setUserName(body_user.get("username"))

