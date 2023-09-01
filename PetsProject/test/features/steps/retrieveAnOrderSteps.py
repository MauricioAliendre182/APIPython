from behave import when
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
import json

@when("a user retrieves a pet order")
def retireve_a_pet_order(context):
    header = {"Content-Type": "application/json; charset=utf-8"}
    resp_value = json.loads(Controller.getResponse().text)
    id = str(resp_value.get('id'))
    Controller.setResponse(APIManager().get(endpoint=f"/store/order/{id}", headers=header))


@when("a user tries to retrieve an unexistant pet order")
def retireve_a_pet_order(context):
    header = {"Content-Type": "application/json; charset=utf-8"}
    id = 13
    Controller.setResponse(APIManager().get(endpoint=f"/store/order/{id}", headers=header))