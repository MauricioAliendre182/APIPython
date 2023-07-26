from behave import when, then
from BDDbehave.src.manager.APIManager import APIManager
from BDDbehave.src.conttroller.controller import Controller
import json

@when("a user creates a pet")
def create_a_pet(context):
    body = {
        "id": 504,
        "category": {
            "id": 504,
            "name": "Pug1"
        },
        "name": "ChocoLO",
        "photoUrls": [
            "Nothing"
        ],
        "tags": [
            {
                "id": 504,
                "name": "Chocolate3"
            }
        ],
        "status": "available"
    }
    header = {"Content-Type": "application/json; charset=utf-8"}
    Controller.setResponse(APIManager().post(endpoint="/pet", headers=header, payload=body))

@when("a user updates a pet")
def update_a_pet(context):
    body = {
        "name": "Choco",
        "status": "available"
    }
    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    resp_value = json.loads(Controller.getResponse().text)
    id = str(resp_value.get('id'))
    print(resp_value)
    print(id)
    Controller.setResponse(APIManager().post(endpoint=f"/pet/{id}", headers=header, payload=body))

@when("a user retrieves a pet")
def retrieve_a_pet(context):
    header = {"Content-Type": "application/json; charset=utf-8"}
    resp_value = json.loads(Controller.getResponse().text)
    id = str(resp_value.get('id'))
    print(resp_value)
    print(id)
    Controller.setResponse(APIManager().get(endpoint=f"/pet/{id}", headers=header))

@when("a user deletes a pet")
def delete_a_pet(context):
    header = {"Content-Type": "application/json; charset=utf-8"}
    resp_value = json.loads(Controller.getResponse().text)
    id = str(resp_value.get('id'))
    print(resp_value)
    print(id)
    Controller.setResponse(APIManager().get(endpoint=f"/pet/{id}", headers=header))

@then('the status code is correct')
def status_code(context):
    print(Controller.getResponse().status_code)
    assert Controller.getResponse().status_code == 200


