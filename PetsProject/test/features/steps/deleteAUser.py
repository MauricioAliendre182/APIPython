from behave import when
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller


@when("a user delete a user created previously")
def delete_a_user(context):
    username = Controller.getUserName()
    header = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().delete(endpoint=f"/user/{username}", headers=header))