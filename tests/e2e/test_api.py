import pytest
import requests
from datetime import datetime, timezone

from .api_client import get_growth_by_name, get_growth_by_age , post_to_add_growth
import pytest


@pytest.mark.usefixtures("restart_api")
def test_path_correct_returns_212_and_Growth_added():

    nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)

    name = f"John"
    Lname= f"Smith"
    head=35
    weight=27
    hight=3
    age=3
    gender= f"boy"
    url = f"http://example.com"
    notes = f"Kids growth"
    date_added = nu.isoformat()
    date_edited = nu.isoformat()

    post_to_add_growth(name,Lname, head,weight,hight,age,gender,url, notes, date_added, date_edited)

    r = get_growth_by_name(name)
    assert r.ok
    assert r.json() == [
        {
            "name": name,
            "Lname":Lname,
            "head":head,
            "weight":weight,
            "hight":hight,
            "age":age,
            "gender":gender,
            "url": url,
            "notes": notes,
        },
    ]



@pytest.mark.usefixtures("restart_api")
def test_incorrect_name__error_message():

    nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)
    name : str= f"John"
    Lname : str= f"Smith"
    head : float=35
    weight : float=27
    hight : float=3
    age: int=2
    gender: str= f"boy"
    url : str = f"http://example.com"
    notes : str= f"Kids growth"
    date_added: str = nu.isoformat()
    date_edited: str = nu.isoformat()
    r = post_to_add_growth(name, Lname,head,weight,hight,age,gender,url, notes, date_added, date_edited)
    assert r.status_code == 400
    assert r.json()["message"] == f"Invalid name {name}"

    r = get_growth_by_name(name)
    assert r.status_code == 404


@pytest.mark.usefixtures("restart_api")
def test_incorrect_age__error_message():

    nu: datetime = datetime(2021, 4, 15, 0, 0, 0, 0, tzinfo=timezone.utc)
    name : str= f"John"
    Lname : str= f"Smith"
    head : float=35
    weight : float=27
    hight : float=3
    age: int=40
    gender: str= f"boy"
    url : str = f"http://example.com"
    notes : str= f"Kids growth"
    date_added: str = nu.isoformat()
    date_edited: str = nu.isoformat()

    
    m = post_to_add_growth(name, Lname,head,weight,hight,age,gender,url, notes, date_added, date_edited)
    assert m.status_code == 400
    assert m.json()["message"] == f"Invalid age {age}"

    m = get_growth_by_age(age)
    assert m.status_code == 404