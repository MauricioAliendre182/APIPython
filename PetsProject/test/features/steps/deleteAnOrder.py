from behave import when
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
import json

@when("a user deletes a pet order")
def delete_a_pet_order(context):
    header = {"Content-Type": "application/json; charset=utf-8"}
    resp_value = json.loads(Controller.getResponse().text)
    id = str(resp_value.get('id'))
    Controller.setResponse(APIManager().delete(endpoint=f"/store/order/{id}", headers=header))


@when("a user tries to delete an unexistant pet order")
def delete_a_pet_order(context):
    header = {"Content-Type": "application/json; charset=utf-8"}
    id = 13
    Controller.setResponse(APIManager().delete(endpoint=f"/store/order/{id}", headers=header))