from PetsProject.src.entity.order import Order
from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
from PetsProject.src.entity.category import Category
from PetsProject.src.entity.tag import Tag
from PetsProject.src.entity.pet import Pet
import dataclasses
import json
from PetsProject.src.methods.DateGenerator import DateGenerator

def before_scenario(scenario, context):
    for tag in scenario.tags:
        if tag in ("UpdateAPet", "DeleteAPet", "RetrieveAPet"):
            body = dataclasses.asdict(
                Pet(
                    id=502,
                    name="Chocolate1",
                    tags=[Tag(502, 'Choco1')],
                    category=Category(502, "Pug1")
                )
            )
            head = {"Content-Type": "application/json; charset=utf-8"}
            Controller.setResponse(APIManager().post(endpoint="/pet", headers=head, payload=body))

        elif tag in ("RetrieveAPetOrder", "UpdateAPetOrder", "DeleteAPetOrder" ):
            body_order = dataclasses.asdict(
                Order(
                    id_order=1,
                    id_pet=1,
                    quantity=30,
                    shipDate=DateGenerator.generateDateInIso8601Format()
                )
            )
            head_order = {"Content-Type": "application/json; charset=utf-8"}
            Controller.setResponse(APIManager().post(endpoint="/store/order", headers=head_order, payload=body_order))

def after_scenario(scenario, context):
    for tag in scenario.tags:
        if tag in ("UpdateAPet", "DeleteAPet", "RetrieveAPet"):
            resp_value = json.loads(Controller.getResponse().text)
            id = str(resp_value.get('id'))
            head = {"Content-Type": "application/json; charset=utf-8"}
            Controller.setResponse(APIManager().delete(endpoint=f"/pet/{id}", headers=head))

        elif tag in ("RetrieveAPetOrder", "UpdateAPetOrder", "DeleteAPetOrder"):
            resp_value_order = json.loads(Controller.getResponse().text)
            id_order = str(resp_value_order.get('id'))
            head = {"Content-Type": "application/json; charset=utf-8"}
            Controller.setResponse(APIManager().delete(endpoint=f"/store/order/{id_order}", headers=head))