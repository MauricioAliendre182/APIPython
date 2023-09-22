from behave import when
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller


@when("a user retrieve the information of a user created")
def get_a_user(context):
    username = Controller.getUserName()
    header = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().get(endpoint=f"/user/{username}", headers=header))

