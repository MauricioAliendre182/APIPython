from PetsProject.src.manager.APIManager import APIManager
from PetsProject.src.conttroller.controller import Controller
from PetsProject.src.entity.category import Category
from PetsProject.src.entity.tag import Tag
from PetsProject.src.entity.pet import Pet
import dataclasses
import json


def before_scenario(scenario, context):
    if "UpdateAPet" or "DeleteAPet" or "RetrieveAPet" in scenario.effective_tags:
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


def after_scenario(scenario, context):
    if "UpdateAPet" or "CreateAPet" or "RetrieveAPet" in scenario.effective_tags:
        resp_value = json.loads(Controller.getResponse().text)
        id = str(resp_value.get('id'))
        head = {"Content-Type": "application/json; charset=utf-8"}
        Controller.setResponse(APIManager().delete(endpoint=f"/pet/{id}", headers=head))
