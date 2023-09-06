from behave import when, then
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
from PetsProject.src.methods.DateGenerator import DateGenerator
from PetsProject.src.entity.user import User
import dataclasses

@when("a user creates a user in the pet store")
def create_a_user(context):
    for row in context.table:
        context.id_user = int(row['id']) if (len(row['id']) > 0 and any(char.isdigit() for char in row['id'])) else row['id']
        context.username = row['username']
        context.firstname = row['firstName']
        context.lastname = row['lastName']
        context.email = row['email']
        context.password = row['password']
        context.phone = int(row['phone'])
        context.userstatus = int(row['userStatus']) if (len(row['userStatus']) > 0 and any(char.isdigit() for char in row['userStatus'])) else row['userStatus']

    body = dataclasses.asdict(
        User(
            id_user=context.id_user,
            username=context.username,
            firstName=context.firstname,
            lastName=context.lastname,
            email=context.email,
            password=context.password,
            phone=context.phone,
            userStatus=context.userstatus
        )
    )
    header = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().post(endpoint="/user", headers=header, payload=body))