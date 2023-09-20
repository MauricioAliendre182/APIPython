
from behave import when
from PetsProject.src.entity.user import User
from PetsProject.src.conttroller.controller import Controller
from PetsProject.src.manager.APIManager import APIManager

@when("multiple users are created using a array")
def create_users_with_array(context):
    context.users_array = []
    usernamesArray = []
    for row in context.table:
        user = User(
            0,
            row['username'],
            row['firstName'],
            row['lastName'],
            row['email'],
            row['password'],
            row['phone'],
            int(row['userStatus'])
        )
        context.users_array.append(user)
    user_list = [user.__dict__ for user in context.users_array]
    usernamesArray = [user.username for user in context.users_array]
    Controller.setArrayUsernames(usernamesArray)
    header = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().post(endpoint="/user/createWithArray", headers=header, payload=user_list))
