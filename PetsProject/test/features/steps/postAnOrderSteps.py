from behave import when, then
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
from PetsProject.src.methods.DateGenerator import DateGenerator
from PetsProject.src.entity.order import Order
import dataclasses

@when("a user stores a pet order")
def create_a_pet_order(context):
    for row in context.table:
        context.id_order = int(row['id_order']) if len(row['id_order']) > 0 else row['id_order']
        context.id_pet = int(row['id_pet'])
        context.quantity = int(row['quantity'])
        context.status = row['status']
        context.complete = bool(row['complete'])

    body = dataclasses.asdict(
        Order(
            id_order=context.id_order,
            id_pet=context.id_pet,
            quantity=context.quantity,
            shipDate=DateGenerator.generateDateInIso8601Format(),
            status=context.status,
            complete=context.complete
        )
    )
    header = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().post(endpoint="/store/order", headers=header, payload=body))

@then('the status code is {statuscode:d}')
def status_code(context, statuscode):
    assert Controller.getResponse().status_code == statuscode