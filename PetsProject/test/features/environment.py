# Example of hooks
# # before all
# def before_all(context):
#    print('Before all executed')
# # before every scenario
# def before_scenario(scenario, context):
#    print('Before scenario executed')
# # after every feature
# def after_feature(scenario, context):
#    print('After feature executed')
# # after all
# def after_all(context):
#    print('After all executed')

from BDDbehave.src.manager.APIManager import APIManager
from BDDbehave.src.conttroller.controller import Controller
import json


def before_scenario(scenario, context):
    if "UpdateAPet" or "DeleteAPet" or "RetrieveAPet" in scenario.effective_tags:
        body = {
            "id": 502,
            "category": {
                "id": 502,
                "name": "Pug1"
            },
            "name": "ChocoLO",
            "photoUrls": [
                "Nothing"
            ],
            "tags": [
                {
                    "id": 502,
                    "name": "Chocolate3"
                }
            ],
            "status": "available"
        }
        head = {"Content-Type": "application/json; charset=utf-8"}
        Controller.setResponse(APIManager().post(endpoint="/pet", headers=head, payload=body))


def after_scenario(scenario, context):
    if "UpdateAPet" or "CreateAPet" or "RetrieveAPet" in scenario.effective_tags:
        resp_value = json.loads(Controller.getResponse().text)
        id = str(resp_value.get('id'))
        print(resp_value)
        print(id)
        head = {"Content-Type": "application/json; charset=utf-8"}
        Controller.setResponse(APIManager().delete(endpoint=f"/pet/{id}", headers=head))
