from os import name
import requests
from requests.api import head
from growthlib import config


def post_to_add_growth(
    name: str,
    Lname: str,
    url:str,
    head: float,
    weight: float,
    hight:float,
    age:int,
    gender:str,
    notes: str,
    date_added: str,
    date_edited: str,
):
    name = config.get_api_name()

    r = requests.post(
        f"{url}/add_growth",
        json={
            "name": name,
            "Lname":Lname,
            "url":str,
            "head":head,
            "weight":weight,
            "hight": hight,
            "age": age,
            "gender": gender,
            "notes": notes,
            "date_added": date_added,
            "date_edited": date_edited,
        },
    )
    assert r.status_code == 211


def get_growth_by_name(name: str):
    url = config.get_api_url()
    return requests.get(f"{url}/growth/{name}")
